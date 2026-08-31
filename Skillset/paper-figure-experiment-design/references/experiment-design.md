# Experiment Design for Figure-Level Claims

## Begin with the decision

Every experiment should reduce a named uncertainty. Before launching it, write:

```text
QUESTION
HYPOTHESIS
PREDICTION
STRONGEST ALTERNATIVE
MANIPULATED VARIABLE
CONTROLLED VARIABLES
METRICS
EXPECTED OUTCOMES
DECISION RULE
STOP CONDITION
```

If the result cannot change a claim, design choice, or next action, do not run the experiment.

## Classify the variables

- **Scientific:** the factors whose effects the paper intends to understand.
- **Nuisance:** factors needed for strong performance but not scientifically interesting.
- **Fixed:** factors held constant because changing them adds little information.
- **Conditional:** factors whose best setting may depend on the scientific choice.

State the manipulated variable in one line. If several scientific variables change together, call the study a bundle comparison and add isolating experiments before making component-level claims.

## Match claims to evidence

| Claim type | Minimum persuasive evidence | Stronger evidence | Frequent confound |
|---|---|---|---|
| Better task performance | strong closest baseline on matched protocol | multiple tasks, backbones, and seeds | different data or tuning effort |
| More efficient | quality-cost Pareto curve | wall-clock, memory, energy, and hardware disclosure | comparing token count alone |
| Mechanism explains gain | component intervention with predicted directional effect | mediation, counterfactual, or targeted perturbation | post-hoc representation plot |
| More stable | learning curves and failure rate across seeds | stress conditions and recovery analysis | reporting only the best run |
| Generalizes | prespecified distribution shift | multiple independent shift axes | near-duplicate test data |
| Scales | at least three meaningful scale points | fitted trend with uncertainty and budget accounting | changing recipes across scale |
| Interpretable | representation predicts a relevant variable | controlled edit changes behavior as predicted | plausible-looking decoded examples |
| Broad capability | task taxonomy plus representative metrics | held-out capabilities and failure analysis | many redundant benchmarks |
| Necessary component | remove or replace one component | matched-capacity and matched-compute alternatives | ablation changes capacity and optimization |

Do not let a main-results table stand in for mechanism, efficiency, stability, and generalization simultaneously. Give each load-bearing claim its own discriminating evidence.

## Build the baseline ladder

Use the smallest ladder that closes the important alternatives:

1. **Reference:** the standard or no-change system.
2. **Closest prior:** the method sharing the same setting and objective.
3. **Simpler alternative:** the cheapest explanation for the gain.
4. **Matched-resource alternative:** same parameters, data, training compute, and inference budget.
5. **Component control:** same system with only the scientific variable changed.
6. **Oracle or upper bound:** only when it clarifies headroom or decision quality.

Reproduce or verify the strongest baseline before tuning the proposed method heavily. If a baseline reproduction is weak, diagnose the discrepancy instead of treating it as a win.

## Sequence experiments by information gain

Prefer this order:

```text
sanity check
-> cheap discriminator
-> matched main comparison
-> mechanism or component test
-> robustness and boundary test
-> scaling and cost confirmation
```

Examples of cheap discriminators:

- freeze the new component;
- replace it with a parameter-matched MLP or random control;
- vary one latent step, depth, horizon, or supervision weight;
- evaluate the condition where the proposed mechanism predicts the largest effect;
- test whether the claimed intermediate signal predicts later success;
- remove privileged training information at evaluation.

Escalate to a large sweep only when the cheap result leaves a consequential uncertainty unresolved.

## Design informative ablations

An ablation should test a mechanism, not inventory code switches. For each component, define:

```text
component -> proposed role -> target variable -> prediction -> falsifying observation
```

Use four useful ablation families:

- **Removal:** Is the component necessary in the full system?
- **Replacement:** Is its claimed structure better than a simpler matched alternative?
- **Dose:** Does changing strength, depth, steps, horizon, or data amount follow the predicted response?
- **Interaction:** Does the component help only with another component or under a specific condition?

Measure the intermediate variable the mechanism claims to change. A final-score drop alone rarely identifies why the component matters.

## Enforce tuning fairness

Compare methods under comparable opportunity to succeed.

- Separate scientific and nuisance hyperparameters.
- Use the same data split, preprocessing, model initialization policy, and evaluation code.
- Match training and inference budgets, or show a Pareto frontier when budgets differ.
- Give baselines a defensible tuning budget and report that budget.
- Tune conditional hyperparameters per scientific setting when interactions are plausible.
- Predeclare checkpoint selection and do not select one method by best validation while another uses the final checkpoint.
- Do not silently change batch size, sequence length, augmentation, or early stopping across methods.

When compute is limited, reduce the scientific search space before reducing baseline fairness.

## Measure reliability, not only peaks

For stochastic training, report enough independent runs to distinguish a systematic effect from noise. Choose seeds before seeing results. Report mean and dispersion, individual points when the count is small, and the fraction of failed runs when failures are meaningful.

Inspect full learning curves for:

- divergence, NaN, or collapse;
- delayed gains that make fixed-step comparisons unfair;
- overfitting or checkpoint-selection bias;
- throughput or memory regressions;
- variance that grows with scale or horizon.

Never mix failed, partial, or mismatched runs with completed runs. Record provenance for every plotted point.

## Test robustness and boundaries

Choose shifts that target the claimed mechanism:

- task difficulty or reasoning depth;
- unseen domain, object, scene, embodiment, or language;
- observation noise, occlusion, missing modality, or distractors;
- sequence length, memory horizon, or action frequency;
- model, data, and compute scale;
- imperfect teachers, labels, rewards, or simulators.

Include conditions where the method should not help. Boundary evidence makes a narrow claim more defensible than an unbounded claim supported only by favorable cases.

## Account for efficiency

Report the resource that matters to deployment and the resource that the method changes. Useful measures include:

```text
quality | generated tokens | sequential steps | latency | throughput
peak memory | training FLOPs | inference FLOPs | parameters | energy
```

State hardware, batch size, precision, compilation, sampling settings, and whether preprocessing is included. If one method shifts cost from inference to training or from online to offline computation, show both sides.

Plot quality against cost. A single speedup number can hide a worse accuracy point or an unmatched operating regime.

## Design result figures

- Use a line plot for dose, scale, time, or budget.
- Use a Pareto plot for quality-cost tradeoffs.
- Use a paired dot or interval plot for matched tasks or seeds.
- Use a matrix or heatmap for two controlled axes.
- Use a small multiple for comparable trajectories.
- Use a table when exact values and several conditions matter more than shape.

Avoid truncated axes for small gains, dual axes without necessity, and bar charts without uncertainty for stochastic results. Mark missing and failed runs explicitly rather than treating them as zero.

## Apply a decision rule

Conclude with one of:

- `ADOPT`: effect is meaningful, reliable, and worth its complexity or cost.
- `REJECT`: the predicted effect is absent or the simpler explanation dominates.
- `HOLD`: evidence is ambiguous and one named discriminator remains.
- `BOUNDARY`: the method works only under a specified condition; narrow the claim.

Do not equate statistical detectability with scientific or practical importance. State what was learned, what alternative was weakened, and which branch should be pruned.
