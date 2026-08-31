# Experiment story grammar

An experiment is a controlled study that resolves a stated uncertainty. A completed run is not necessarily valid evidence.

## Declare the contract

Before a load-bearing study, fill this in:

```text
QUESTION
CLAIM OR HYPOTHESIS
PREDICTION
STRONGEST ALTERNATIVE
MANIPULATED VARIABLE
CONTROLLED VARIABLES
INFERENCE UNIT
METRICS
EXPECTED OUTCOMES
DECISION RULE
STOP CONDITION
```

If no plausible outcome would change a belief, claim, or next action, do not run the experiment.

## Classify variables

- `Scientific`: the factor whose effect or mechanism is under study.
- `Nuisance`: matters for performance but is not the claim; tune fairly.
- `Fixed`: held constant by justified convention or resource constraint.
- `Conditional`: only meaningful under a branch of the design.

Changing several scientific variables at once estimates a package effect. Call it that. Do not present it as a component mechanism.

## Map claim types to evidence

| Claim type | Minimum credible evidence | Stronger evidence | Common overclaim |
|---|---|---|---|
| Performance | Strong incumbent and simple baseline under same protocol | Multiple tasks, seeds, and backbones | One best checkpoint or selective task subset |
| Mechanism | Targeted intervention and negative control | Mediation chain, rescue, and dose response | Component removal alone |
| Generalization | Predefined held-out axis | Multiple independent axes and model families | More examples from the training distribution |
| Efficiency | Quality-matched latency, memory, or compute | Pareto frontier with matched tuning | FLOPs alone or unmatched accuracy |
| Robustness | Controlled stressor sweep | Recovery test and boundary analysis | One adversarial example |
| Necessity | Removal under otherwise valid operation | Substitution and rescue | Performance drop after breaking the system |
| Sufficiency | Add factor to a setting that lacks it | Cross-context replication | Correlation or decodability |

## Choose baselines by explanation

Baseline selection should cover alternative explanations, not just recognizable names.

1. `No-op/current input`: what happens without the claimed resource?
2. `Simple heuristic`: can a cheap rule explain the gain?
3. `Matched architecture`: is extra capacity or training enough?
4. `Substitute mechanism`: does another mechanism recover the same effect?
5. `Strong incumbent`: does the method improve the best relevant existing approach?
6. `Oracle or upper bound`: is the bottleneck worth solving?
7. `Compute- or quality-matched`: is the tradeoff actually favorable?

Use a factorial design when the claim is about an interaction. Report main effects and interaction rather than only the best cell.

## Build a diagnostic chain

For a multi-stage mechanism, measure the stages between input and headline outcome:

```text
availability -> representation -> retention -> retrieval or selection
-> action or prediction -> task return -> resource cost
```

Use interventions to distinguish stages:

- zero or mask the signal;
- shuffle it within a valid comparison set;
- substitute a donor signal;
- delete or delay it;
- supply an oracle;
- force retention or retrieval;
- vary dose, budget, delay, or distractors;
- test whether performance recovers when the hypothesized bottleneck is repaired.

Decodability does not establish action causality. A drop after a bundled removal establishes system dependence, not the isolated role of one path.

## Organize the experiment suite

Use only families that pay a claim debt:

- `Main comparison`: external performance under a common protocol.
- `Isolation`: component or interface differences.
- `Causal test`: controlled intervention, negative control, rescue.
- `Stress curve`: delay, noise, budget, capacity, or distractor sweep.
- `Generalization`: predefined domain, task, embodiment, or backbone shift.
- `Efficiency`: latency, throughput, memory, training cost, Pareto frontier.
- `Reliability`: seeds, task-level variation, confidence intervals, failure rates.
- `Failure analysis`: boundary conditions and classified failures.

Scale a controlled variable within the same task or identity when possible. Cross-task scaling often confounds task difficulty with the intended axis.

## Enforce tuning fairness

For all compared methods, document and match where relevant:

- data versions, preprocessing, splits, and augmentations;
- training examples, updates, optimizer budget, and early stopping;
- hyperparameter search space, number of trials, and selection rule;
- checkpoint-selection metric and access to validation or test data;
- pretrained weights, backbone capacity, context, and external data;
- inference calls, samples, tokens, memory, latency, and hardware;
- evaluation seeds, trials, task instances, and failure handling.

A cross-paper SOTA table is contextual unless inputs, pretraining, data, compute, action or output space, checkpoint selection, and evaluation are genuinely comparable. Do not use contextual rankings for a controlled superiority claim.

An identical hyperparameter is not always fair; comparable tuning opportunity is the goal. Conversely, method-specific tuning is not evidence of unfairness if budgets and selection rules are comparable and disclosed.

Separate:

- discovery runs used to choose the method;
- tuning runs used to set nuisance variables;
- sealed confirmation used to estimate the final effect.

Never select and report the same test outcome as confirmatory evidence.

## Quantify uncertainty at the right level

- Define the inference unit: seed, task, environment, participant, episode, or paired instance.
- Prefer paired differences when methods share instances and randomness.
- Report effect sizes and confidence intervals, not only means or significance.
- Show distributions or per-task effects when averages can hide reversals.
- Use equivalence or non-inferiority tests for “same quality” claims.
- Predeclare practical margins where they affect the decision.
- Report failed, invalid, and excluded runs with reasons. Quarantine them from valid aggregates.
- Distinguish binary success, partial progress, reward proxies, and human scores.
- Inspect the complete subgroup grid for direction reversals before reporting an aggregate.

Do not treat repeated episodes from one trained checkpoint as independent evidence about training variance.

## Verify before trust

Check:

```text
provenance known
configuration matches intent
run complete
metric count correct
no NaN, silent fallback, or failed-run contamination
selection protocol legal
comparison fair enough for stated claim
alternative explanations addressed
claim wording matches evidence strength
```

Label outputs `TRUSTED`, `CANDIDATE`, `FAILED`, or `UNKNOWN`. Only trusted evidence may feed the paper's headline figure or conclusion.
