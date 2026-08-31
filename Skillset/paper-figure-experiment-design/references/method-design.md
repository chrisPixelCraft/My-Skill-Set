# Designing the Scientific Method

## Localize the failure before proposing a module

Write the failure as a conditional observation:

```text
Under condition C, baseline B fails on behavior Y,
and diagnostic D suggests bottleneck Z.
```

Then distinguish:

- **phenomenon:** what is directly observed;
- **cause hypothesis:** what may generate it;
- **intervention target:** what can be changed;
- **success variable:** what should move first if the hypothesis is right;
- **task outcome:** what ultimately matters.

Do not skip from phenomenon to architecture. A method derived from an unlocalized problem tends to accumulate decorative components and produces uninterpretable ablations.

## Choose the primary intervention family

| Failure signature | Common intervention | Why it can work | New risk | Decisive test |
|---|---|---|---|---|
| Discrete or linguistic bottleneck | continuous, latent, spatial, or multimodal representation | increases bandwidth or preserves nonverbal structure | opacity, drift, collapse | decode, intervene on, or perturb the claimed information |
| Too little or too much computation | recurrence, early exit, adaptive depth, selective or parallel compute | allocates reasoning where useful | overthinking, routing overhead, unstable depth | quality-cost curve plus oracle or policy analysis |
| Coarse or delayed learning signal | step-, process-, trajectory-, or stage-aware supervision | assigns credit nearer the relevant state | teacher bias, annotation cost, reduced diversity | compare supervision granularity under matched data and compute |
| Outcome-only optimization | process rewards, correctors, auxiliary objectives, regularization | stabilizes intermediate behavior | reward hacking, dependence on evaluator | remove or corrupt guidance and measure predicted collapse |
| Missing history | symbolic, perceptual, recurrent, or external memory | makes task-relevant past information accessible | context cost, stale or lossy memory | representation-by-integration factorial test across memory demands |
| One path for heterogeneous cases | routing, hybrid explicit/latent modes, slow-fast experts | specializes computation by state or difficulty | router confound, load imbalance | matched always-on paths, oracle router, and routing calibration |
| Heterogeneous data are pooled or discarded | assign data sources distinct targets or objectives | extracts complementary supervision | data-quality leakage, objective confounding | data-source-by-objective ablation and held-out transfer |
| Prediction is weakly grounded | spatial, visual, action, or environment-aligned targets | ties internal state to executable structure | privileged information and simulator bias | remove privileged targets and test cross-environment behavior |

Pick the family whose mechanism most directly changes the localized variable. Combining families is justified only when one enables another and the interaction is tested.

## Specify the mechanism chain

Fill each field with a measurable noun or verb:

```text
BASELINE STATE:
FAILURE CONDITION:
TARGET VARIABLE:
INTERVENTION OPERATOR:
IMMEDIATE EFFECT:
DOWNSTREAM EFFECT:
MEASUREMENT:
FALSIFIER:
BOUNDARY CONDITION:
```

Example structure:

```text
more latent steps -> states homogenize -> supervise each state against its step
-> state diversity remains high -> reasoning remains stable at larger step budgets
```

This is a hypothesis chain, not proof. Each arrow needs either prior evidence or a planned experiment.

## Keep one load-bearing novelty

Classify every component as:

- **scientific:** carries the main hypothesis;
- **enabling:** required to make the scientific component operational;
- **stabilizing:** prevents a known optimization or systems failure;
- **convenience:** implementation choice with no intended scientific claim.

The paper should foreground one primary scientific component. If several are necessary, state whether the contribution is a system bundle and avoid attributing the full gain to any single part.

For each added component, answer:

```text
What unique failure does it address?
What simpler replacement could serve the same role?
What capacity, data, compute, or supervision does it add?
What new failure mode does it create?
What result would make us remove it?
```

## Design the interface, not only the block

A research method is often distinguished by where it intervenes.

- **Representation seam:** between observation or token and hidden state.
- **Temporal seam:** between recurrent steps, history, or action frequencies.
- **Learning seam:** between target, loss, reward, and parameter update.
- **Control seam:** between a router or policy and alternative computation paths.
- **Memory seam:** between stored history, retrieval, integration, and action.
- **Deployment seam:** between training-only privilege and inference-time inputs.

Choose the narrowest seam that exposes the intended variable and preserves a strong matched control. A deep interface hides unnecessary machinery and makes causal attribution harder.

## Use training–inference asymmetry carefully

Teachers, privileged modalities, auxiliary decoders, simulators, and process labels can shape representations during training and disappear at inference. This is attractive because it can add supervision without deployment cost.

Audit four risks:

- privileged data may make the comparison unfair;
- the student may imitate teacher artifacts rather than the desired mechanism;
- removed modules may still shift training compute or data cost substantially;
- train–test mismatch may appear under novel conditions.

Show the asymmetry explicitly in the method figure and isolate it experimentally.

## Design temporal and adaptive methods

For recurrent, multi-rate, or selectively routed methods, define:

```text
state carried forward
update frequency
information available at each step
stopping or routing rule
parameter sharing
worst-case compute
failure on stale or skipped state
```

Adaptive compute requires both an upper-bound question—can selection help?—and a policy question—can the learned selector realize that benefit without excessive overhead? Report average and tail compute, not only the mean.

## Design memory methods as a matrix

Separate memory representation from memory integration.

```text
representation: symbolic | perceptual | recurrent | external
integration: context | modulation | dedicated memory operator
```

Crossing these axes prevents a representation gain from being confused with an integration gain. Evaluate against task demands such as temporal, spatial, object, and procedural memory rather than only aggregate success.

## Design data-centric methods by role

When data sources differ in quality, modality, or labels, state what each source is allowed to teach:

```text
source -> target -> objective -> model component -> expected transfer
```

Do not infer that more data caused the gain when data type, objective, and scale all changed. Use matched subsets, data-dose curves, and source-by-objective ablations.

## Pre-mortem the method

Before implementation, list the three most plausible failures. Common ones include:

- the diagnostic is correlational and the intervention targets the wrong cause;
- added capacity or compute, not the claimed structure, explains the gain;
- an auxiliary loss improves the proxy while hurting the task;
- routing collapses to one path or exploits task identity;
- latent state becomes homogeneous, ungrounded, or uninterpretable;
- memory grows without improving task-relevant recall;
- privileged supervision leaks information unavailable at deployment;
- the method helps only one favorable scale or benchmark.

For each, specify the cheapest observation that would reveal it. Build those signals into training logs and early experiments.

## Decide whether the method is ready

Advance the design only when:

- the failure is reproducible;
- the target variable is measurable;
- the intervention is smaller than the explanation it tests;
- the strongest simple alternative has a planned control;
- expected benefits and new costs are explicit;
- at least one result could falsify the mechanism;
- the diagram and experiment matrix describe the same method.

Otherwise redesign the hypothesis or measurement before expanding the architecture.
