# 7W questions and templates

Use all seven question families, but keep only questions that can change the design.

## Teaser questions

| Lens | Ask |
|---|---|
| What | What single tension and contribution must survive a five-second glance? |
| Why | Why does the incumbent fail, and why does that failure matter? |
| How | How is failure -> intervention -> consequence encoded visually? |
| Where | Where in the system, environment, space, or timeline does the gap occur? |
| When | When does information appear, disappear, update, or become useful? |
| Who | Who is the intended reader, and who acts, observes, stores, selects, supervises, or benefits? |
| Which | Which alternative, comparison axis, example, or result is decisive? |

## Method-figure questions

| Lens | Ask |
|---|---|
| What | What are the inputs, states, operations, outputs, and objectives? |
| Why | Why does each component exist; which failure or hypothesis requires it? |
| How | How do information, state, control, gradient, loss, and reward flow? |
| Where | Where is the novelty seam, bottleneck, supervision, or privileged input? |
| When | When do training, inference, read, write, reset, and updates occur? |
| Who | Who is trainable, frozen, shared, oracle, controller, evaluator, or environment? |
| Which | Which path is baseline, proposed, optional, conditional, or deployment-only? |

## Experiment questions

| Lens | Ask |
|---|---|
| What | What claim, estimand, manipulated variable, and metric are tested? |
| Why | Why is this the cheapest decision-relevant discriminator? |
| How | How are controls, tuning, statistics, decision rules, and recovery defined? |
| Where | Where are data, tasks, domains, backbones, and ID/OOD boundaries? |
| When | When are tuning, checkpoint selection, intervention, and confirmation performed? |
| Who | Who or what is the inference unit, evaluator, seed, task, or subject? |
| Which | Which incumbent, heuristic, oracle, negative control, and search space are required? |

Under `How`, also ask how much: effect size, variance, data, trials, latency, compute, memory, and control rate.

## Corpus comparison template

| Paper | Figure role | One-message burden | Archetype | Context | Distinctive element | Evidence link | Strength | Risk | Transfer rule |
|---|---|---|---|---|---|---|---|---|---|

After the table, synthesize:

- stable patterns across contexts;
- differences explained by claim type;
- counterexamples that break the pattern;
- design rules worth transferring;
- conventions that should not be copied.

## Storyboard template

```text
Paper burden:
Dominant archetype:
Rejected alternative and why:

Panel A — context or setup
  message:
  actors and objects:
  visual encoding:

Panel B — failure or missing property
  message:
  controlled contrast:
  risk of overclaim:

Panel C — proposed delta
  message:
  novelty seam:
  visual encoding:

Panel D — consequence or evidence, only if justified
  metric and baseline:
  uncertainty and scope:

Reading order:
Legend:
Five-second sentence:
Caption draft:
```

Compact wireframe example:

```text
[earlier cue] --time--> [same current view]
      |                       |
      v                       v
[baseline forgets]      [ours retains/selects]
      |                       |
      +------ failure vs success -----+
```

The wireframe specifies relationships, not final styling.

## Method specification template

```text
Scope and phase:
Main path:
Novelty seam:
State lifecycle:
Train-only paths:
Inference-only paths:
Frozen/trainable/oracle roles:
Arrow semantics:
Color and shape semantics:
Capacity, cadence, and reset:
Items intentionally omitted:
Source checks required:
```

## Claim-to-experiment matrix

| ID | Claim | Prerequisite/readiness | Strongest alternative | Manipulation | Controls | Baselines | Metrics | Inference unit | Decision rule | Stop condition | Figure/table | Trust |
|---|---|---|---|---|---|---|---|---|---|---|---|---|

Keep one row per atomic claim. If several claims point to the same experiment, state exactly which contrasts answer each claim.

## Audit output template

```text
OUTCOME
  Current story and whether it is defensible.

LOAD-BEARING GAPS
  Gap -> evidence -> consequence -> smallest repair.

TEASER
  Five-second message, chosen grammar, storyboard, risks.

METHOD FIGURE
  Novelty seam, paths, timing, roles, missing semantics.

EXPERIMENTS
  Claim matrix, fairness risks, missing controls, stop rules.

REMAINING UNKNOWN
  Only uncertainties that can change a decision.

GATE REPORT
  PASS / CONDITIONAL / FAIL / UNKNOWN for each applicable verifier gate.
```
