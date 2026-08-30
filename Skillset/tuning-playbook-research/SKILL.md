---
name: tuning-playbook-research
description: Apply a scientific, incremental deep-learning experimentation and hyperparameter-tuning protocol derived from Google Research's Deep Learning Tuning Playbook. Use when Codex is asked to plan, review, debug, compare, tune, or interpret ML/DL training experiments; design ablations or baselines; classify scientific/nuisance/fixed hyperparameters; choose search spaces and trial budgets; inspect training curves; handle variance; select checkpoints; or decide whether evidence justifies adopting a model/training change. Also use when a research result may be confounded by tuning fairness, random seeds, training budget, evaluation design, or pipeline complexity. Do not use as a generic literature-survey skill when no empirical training or experiment decision is involved.
---
# Tuning Playbook Research Protocol
## Purpose
Turn model development from trial-and-error into an evidence-driven experimental loop.

The governing priorities are:

1. Learn enough about the problem to make better decisions.
2. Make comparisons fair before interpreting them.
3. Prefer simple, reliable baselines before adding complexity.
4. Treat hyperparameter tuning as part of experimental design, not as an afterthought.
5. Distinguish real improvements from trial, search, and data variance.
6. Adopt complexity only when the evidence and benefit justify it.

This skill is a procedural adaptation of the **Deep Learning Tuning Playbook** by Varun Godbole, George E. Dahl, Justin Gilmer, Christopher J. Shallue, and Zachary Nado. It is not an official Google product. The instructions below are deliberately paraphrased rather than copied verbatim.
## Non-goals
Do not:

- blindly maximize a validation metric without understanding the tuning problem;
- treat one lucky run as proof;
- compare methods with obviously unequal tuning effort when the conclusion depends on fair tuning;
- change many scientifically meaningful factors at once unless the user explicitly wants a bundled engineering comparison;
- present hidden chain-of-thought. Give conclusions, concise rationale, observable evidence, assumptions, and uncertainty instead;
- claim that a recommendation from the playbook is universal truth. Treat it as a strong operating heuristic that must be checked against the workload.
## Progressive disclosure
Read only the references needed for the task:

- New project, baseline, optimizer, batch size, initial configuration: `references/project_start.md`
- Experimental rounds, variable roles, studies, search spaces, plots, exploration/exploitation, adoption decisions: `references/scientific_tuning.md`
- Training length, compute-bound tuning, input pipeline, evaluation, checkpoints, tracking, BatchNorm, multi-host: `references/training_pipeline.md`
- Failure diagnosis, instability, overfitting, variance, unfair comparisons, debugging: `references/failure_diagnosis.md`
- Copy-ready plan/review/decision formats: `references/templates.md`
- Mapping back to the original playbook and scope notes: `references/source_map.md`

For a substantial experiment-design task, read `scientific_tuning.md` plus whichever domain reference is relevant. For a result-review task, read `scientific_tuning.md` and `failure_diagnosis.md`. For a new training pipeline, read `project_start.md` and `training_pipeline.md`.
## Operating modes
Infer the mode from the request. If ambiguous, use the smallest mode that can answer the request.
### PLAN
Use when designing the next experiment or experiment round.

Produce:

- research question;
- incumbent/baseline;
- scientific variables;
- nuisance variables;
- fixed variables and resulting caveats;
- conditional variables if present;
- study/trial design;
- search spaces and scales;
- metrics and evaluation cadence;
- training budget;
- variance/repeat plan;
- adoption/rejection criteria;
- expected diagnostic plots;
- likely failure modes.
### REVIEW
Use when the user already has an experiment plan or result.

Check:

- whether the experiment answers a single interpretable question;
- whether baseline and candidate received fair tuning;
- whether nuisance variables were optimized enough;
- whether fixed choices limit the claim;
- whether search boundaries were hit;
- whether the best result could be a lucky trial;
- whether curves reveal overfitting, undertraining, instability, or bugs;
- whether evaluation and checkpoint selection are comparable;
- whether the claimed improvement exceeds the relevant variance and complexity cost.
### DIAGNOSE
Use when training is unstable, slow, inconsistent, or unexpectedly bad.

Diagnose in this order unless evidence strongly suggests another order:

1. Measurement/evaluation correctness.
2. Data/input pipeline correctness.
3. Training pipeline correctness.
4. Optimization stability.
5. Search-space adequacy.
6. Training duration/budget.
7. Regularization/overfitting.
8. Architecture/method hypothesis.

Do not immediately invent a new method when a pipeline or measurement issue can explain the symptom.
### DECIDE
Use when deciding whether to adopt a candidate change.

Classify the decision as:

- **ADOPT**: evidence supports a real improvement and benefit exceeds complexity cost;
- **REJECT**: evidence indicates no useful improvement or a worse tradeoff;
- **HOLD**: evidence is insufficient or confounded; specify the smallest experiment needed to resolve it.
## Core protocol
### Step 0 — Verify prerequisites
Before tuning, confirm that the following are sufficiently stable for the current question:

- problem formulation;
- dataset and splits;
- primary metric;
- training pipeline;
- evaluation pipeline;
- a configuration that trains and obtains a nontrivial result;
- ability to launch and reproduce runs;
- enough compute to run meaningful comparisons.

If these are not true, switch from performance tuning to **pipeline stabilization**. Do not optimize a broken measurement system.
### Step 1 — Define the objective
State the real objective before choosing experiments.

Possible objectives include:

- learn whether a proposed component helps;
- understand sensitivity to a hyperparameter;
- compare model families;
- reduce training time or resource cost while preserving quality;
- maximize validation performance before a deadline;
- produce the strongest final configuration after an exploration phase.

Keep the experimental question narrow enough that the result can be interpreted.

Bad:

> Try a new architecture, augmentation, optimizer, and schedule and see whether the score improves.

Better:

> Determine whether component X improves the best achievable validation metric when learning rate and regularization are fairly re-tuned.
### Step 2 — Establish the incumbent
The incumbent is the configuration against which new changes are judged.

Prefer:

- a well-established architecture close to the workload;
- a commonly used optimizer for the workload;
- a simple pipeline;
- a relatively fast and resource-efficient initial configuration;
- performance that is clearly meaningful, even if not yet competitive.

Avoid loading the initial baseline with optional tricks. Complexity introduced before it is justified becomes difficult to disentangle later.
### Step 3 — Classify every relevant variable
For the current experimental question, classify hyperparameters and design choices as:
#### Scientific
The variable whose effect the experiment is trying to understand.

Examples:

- number of layers;
- presence of a memory module;
- regularizer type;
- optimizer family;
- augmentation method.
#### Nuisance
A variable that must be tuned or optimized over so different scientific settings can be compared fairly.

Examples often include:

- learning rate;
- regularization strength;
- momentum;
- optimizer-specific parameters;
- schedule parameters.

A nuisance variable is not unimportant. It is precisely important enough that fixing it could bias the scientific comparison.
#### Fixed
A variable held constant for this round.

Every fixed variable creates a caveat: the conclusion is only established under, or near, the fixed setting unless prior evidence supports broader invariance.
#### Conditional
A variable that only exists for some scientific settings.

Do not assume identically named conditional variables share the same useful range. For example, a learning-rate range that works for one optimizer may be inappropriate for another.
### Step 4 — Reduce nuisance variables deliberately
With unlimited resources, many non-scientific variables could be optimized. In reality, an overly large nuisance space becomes too sparse to search well.

Convert a nuisance variable to fixed only when at least one is true:

- prior experiments show the conclusion is insensitive to it;
- domain evidence strongly supports a narrow value;
- compute budget makes tuning it impossible and the caveat is explicitly accepted;
- fixing it is necessary to isolate the current question.

Record the resulting limitation in the final interpretation.
### Step 5 — Design studies, not isolated runs
A **trial** is one concrete configuration/run.

A **study** is a planned set of trials intended to answer an experimental question.

A fair scientific comparison generally requires:

- multiple values/settings of the scientific variable;
- nuisance tuning for each relevant scientific setting;
- comparable trial budgets;
- comparable evaluation and checkpoint-selection rules.

Do not compare "best tuned A" against "default B" and infer that A is scientifically superior.
### Step 6 — Allocate the finite experiment budget
Balance three competing goals:

1. Cover enough values of the scientific variable.
2. Give nuisance variables a broad enough plausible search space.
3. Sample that nuisance space densely enough to find good regions.

More coverage, more dimensions, and more density all cost trials. Make the tradeoff explicit.

When compute is limited, prefer an experiment that answers a narrower question reliably over one that gestures at many questions weakly.
### Step 7 — Choose search spaces scientifically
For each tuned hyperparameter:

- choose a range based on prior evidence, pilot runs, or standard practice;
- use log-like scaling for scale parameters spanning orders of magnitude;
- use linear-like scaling when equal absolute changes are meaningful;
- inspect whether the best trials accumulate at a boundary;
- if a boundary appears optimal, expand the range before concluding that the optimum was found;
- remove ranges that repeatedly generate invalid or obviously broken trials unless the failure itself is informative.

During exploration, prefer interpretable coverage over premature optimization of a narrow region.
### Step 8 — Prefer exploration before exploitation
Most research rounds should primarily increase understanding.

Exploration should reveal:

- which variables matter most;
- which variables interact;
- which variables can safely be fixed later;
- which features are useless and can be removed;
- whether overfitting or undertraining is the current bottleneck;
- where useful regions of the search space lie;
- whether tuning gains appear saturated.

Only after the structure of the problem is reasonably understood should the workflow shift toward greedily finding a single best configuration.
### Step 9 — Run and track reproducibly
Every study should retain at least:

- study name;
- short purpose/notes;
- exact configuration source;
- code revision if available;
- number of trials;
- seeds;
- launch/reproduction command;
- important environment or uncommitted-code notes;
- best validation result;
- checkpoint associated with that result;
- relevant artifacts/plots.

If the information required to reproduce a result is missing, lower confidence in that result.
### Step 10 — Evaluate at comparable step intervals
Prefer evaluation at regular training-step intervals rather than wall-clock intervals.

Reasons include:

- curves become easier to compare;
- preemption, I/O stalls, and network variation do not distort evaluation positions;
- step-periodic artifacts can expose data or shuffling bugs.

Use an evaluation batch size at least as large as training when feasible, because gradients/activation storage are unnecessary during evaluation.
### Step 11 — Save checkpoints and select retrospectively
Train for a predetermined step budget within a study and save checkpoints frequently enough to recover the best validation point.

Do not assume the last checkpoint is best.

Use the same checkpoint-selection rule across compared settings.

Do not use `max_train_steps` as an ordinary tuned hyperparameter inside the same study. Choose a common budget, inspect where best checkpoints occur, then revise the budget in a later round if needed.
### Step 12 — Inspect curves, not only scalar scores
For at least the best few trials of each study, inspect training and validation curves.

Ask:

- Does validation performance degrade while training performance improves? -> overfitting.
- Is the trial still improving at the end? -> possibly compute-bound/undertrained.
- Did both training and validation saturate very early? -> step budget may be wasteful.
- Is there excessive step-to-step fluctuation? -> consider batch noise, validation sample size, late learning rate, or related causes.
- Does training loss rise unexpectedly? -> suspect a bug or instability before proposing new science.
- Are there abrupt spikes or divergences? -> inspect learning rate, warmup, gradient norms, numerical issues, and clipping.

Automate curve and hyperparameter-axis plotting when possible. Friction in plotting reduces the probability that researchers inspect the evidence.
### Step 13 — Use isolation-style comparisons
When comparing values of a scientific variable, summarize each scientific setting by its best result after nuisance optimization.

This supports an apples-to-apples comparison of the scientific variable rather than comparing arbitrary nuisance configurations.

If baseline and candidate require nuisance tuning, both must receive comparable care.
### Step 14 — Characterize variance before adopting changes
Distinguish at least:
#### Trial/retrain variance
Variation between runs using the same hyperparameters but different random seeds or stochastic events.

Potential sources:

- initialization;
- sample order;
- augmentation randomness;
- dropout masks;
- nondeterministic parallel arithmetic.
#### Study/search variance
Variation in the best selected result caused by the hyperparameter search procedure itself.
#### Data/sampling variance
Variation from data generation, train/validation/test splits, or evaluation sampling.

When the decision matters, repeat the best candidate and incumbent enough to estimate the scale of run-to-run variation. Do not demand impossible certainty, but do not mistake a change smaller than ordinary variation for a robust improvement.
### Step 15 — Charge a complexity tax
A candidate change must beat more than the metric.

Account for:

- extra code paths;
- additional hyperparameters;
- more tuning burden;
- slower training/inference;
- memory cost;
- operational fragility;
- harder reproducibility;
- interactions with future experiments.

A tiny noisy gain rarely justifies permanent complexity.
### Step 16 — Decide and update the baseline
Adopt a change when:

- the comparison is sufficiently fair;
- the improvement is credible relative to variance;
- the relevant search spaces were not obviously truncated;
- curves do not reveal a hidden failure;
- the gain is worth the added complexity/cost;
- the conclusion matches the scope of the experiment.

After adoption, the candidate becomes the new incumbent for future rounds.

If evidence is weak, mark **HOLD** and design the smallest resolving study instead of arguing from intuition.
### Step 17 — Shift to exploitation only after exploration is mature
Once:

- useful hyperparameters are known;
- search spaces are refined;
- irrelevant variables have been fixed or removed;
- interactions are understood well enough;

then concentrate the final search around promising regions. More adaptive black-box optimization can become attractive in this phase when the tooling and sequential budget support it.
## Special rules
### Architecture
For a new project, start from an architecture known to work on a similar problem when possible. Custom architecture is justified later when the research question requires it.
### Optimizer
Start from a popular, established optimizer for the workload. Remember that comparing optimizers fairly may require separate nuisance tuning for each optimizer because their useful learning-rate and auxiliary-parameter ranges differ.
### Batch size
Treat batch size primarily as a throughput/resource decision, not as a knob to directly maximize validation performance.

Check:

- hardware feasibility;
- throughput;
- time per training run;
- total resource consumption;
- whether pipeline changes needed for larger batch sizes introduce new bugs or complexity.

When a larger batch does not reduce training time or improve resource tradeoffs, it has little operational value merely because it is larger.
### Training duration
If not compute-bound, train long enough to reveal the best achievable checkpoint but avoid obviously wasteful budgets.

If best checkpoints cluster near the beginning, reduce the budget in a later round.

If they cluster near the end and curves are still improving, consider longer training and re-tuning schedule parameters.

If compute-bound, use many shorter exploratory runs to learn efficiently and reserve long production-length runs for the strongest candidates. Revalidate that conclusions transfer when run length changes.
### Search algorithm
During broad exploration, prefer simple, parallel-friendly, interpretable sampling such as quasi-random search when available.

Do not attribute magical power to the optimizer of the search itself. Search-space design and budget can dominate the difference between search algorithms.

Adaptive Bayesian optimization becomes more attractive when:

- the search space is already refined;
- trial parallelism is limited;
- many trials can be run sequentially;
- the team can operate the optimizer correctly.
### Input pipeline
If accelerators are starved, profile before guessing.

Common causes include:

- remote/network I/O;
- expensive online preprocessing;
- synchronization barriers;
- insufficient prefetching;
- carrying unused features;
- insufficient parallel example generation.

Optimization that makes the pipeline harder to trust is not automatically worthwhile.
### Multi-host training
Treat multi-host as a correctness risk as well as a speed feature.

Audit:

- single-writer logging/checkpointing;
- synchronized statistics where required;
- RNG semantics: same seeds where identical state is required, different seeds where independent data/randomness is required;
- data sharding;
- evaluation consistency.
### Batch normalization
When BatchNorm is involved, verify how statistics are computed and synchronized. Batch-size or host-count comparisons can silently change normalization behavior and invalidate the intended comparison.
## Evidence discipline
When code, configs, logs, plots, or papers are available, ground recommendations in observable evidence.

Prefer statements of the form:

- **Conclusion:** what the experiment supports.
- **Why:** concise causal or methodological rationale.
- **Evidence:** metric, curve, config, run, code path, or source.
- **Caveat:** fixed choices, variance, missing controls, or other limits.

Do not fabricate run results or claim a study was performed when only a plan exists.
## Default response format
For experiment-design and review tasks, use this structure unless the user requests another format:
### Conclusion
One short decision or recommended direction.
### Experimental question
One falsifiable or decision-relevant question.
### Baseline and comparison
Incumbent, candidate, and fairness requirements.
### Variables
| Role | Variables | Treatment |
|---|---|---|
| Scientific | ... | Compare |
| Nuisance | ... | Tune/optimize |
| Fixed | ... | Hold constant; state caveat |
| Conditional | ... | Separate range by scientific setting |
### Study design
Trials, search ranges, run length, metrics, checkpointing, seeds, budget.
### Diagnostics
Curves, search-boundary checks, overfitting, instability, data/eval sanity checks.
### Decision rule
ADOPT / REJECT / HOLD criteria.
### Next experiment
The smallest experiment that provides the most useful new information.
## Final self-check
Before finalizing any recommendation, verify:

- [ ] Is the experimental question narrow enough to interpret?
- [ ] Is there a credible incumbent?
- [ ] Are scientific, nuisance, fixed, and conditional variables classified correctly?
- [ ] Could a fixed variable make the comparison unfair?
- [ ] Are nuisance search spaces broad and dense enough for the claim?
- [ ] Did both sides receive comparable tuning effort?
- [ ] Is the metric/evaluation procedure comparable?
- [ ] Is checkpoint selection comparable?
- [ ] Did we inspect training/validation curves?
- [ ] Are any best points at search boundaries?
- [ ] Could trial/search/data variance explain the gain?
- [ ] Does the gain outweigh added complexity and resource cost?
- [ ] Is the final claim no broader than the evidence?
- [ ] Is the next experiment chosen for information gain rather than habit?
