# 5W2H Audit and Design Templates

Use the questions to expose missing decisions. Do not answer every question in every figure; select the ones that change the design.

## Ask 5W2H of the research story

| Lens | Teaser or motivation | Method figure | Experiments |
|---|---|---|---|
| What | What observable problem and promised change? | What are the inputs, states, operations, and outputs? | What construct, metric, and comparison test the claim? |
| Why | Why does the gap matter, and why is it unresolved? | Why should this component affect the target behavior? | Why can this result distinguish the hypothesis from its alternative? |
| Who | Who or what is affected: user, model, agent, task, or subgroup? | Who produces supervision, consumes outputs, or controls routing? | Which population of tasks, seeds, models, users, or environments is represented? |
| Where | Where does the failure occur? | Where in the pipeline is the intervention applied? | Where does the effect hold or break across domains and conditions? |
| When | When does the failure emerge? | When does each stage run: pretraining, tuning, inference, or each time step? | When is the checkpoint selected, metric measured, and stop rule applied? |
| Which | Which alternative, component, state, or pathway is load-bearing? | Which modules are shared, frozen, trainable, optional, or removed? | Which baseline, ablation, shift, and metric are decisive? |
| How | How does the mechanism transform information or allocate compute? | How do data, state, control, and supervision flow? | How are variables manipulated, confounds controlled, and uncertainty estimated? |

Add **How much** whenever magnitude matters: effect size, compute, latency, data, memory, variance, or annotation cost.

## Create a pattern map

Use one row per distinct figure strategy, not one row per paper when several papers repeat the same idea.

| Pattern | Representative evidence | Shared elements | Important difference | Why it works | Cost or risk | Use when |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

After filling the table, write:

```text
Invariant:
Boundary condition:
Rejected pattern:
Design implication:
```

## Draft the teaser brief

```text
PRIMARY JOB:
ONE-SENTENCE TAKEAWAY:
TARGET READER:
CONTEXT THEY ALREADY KNOW:
CONTEXT THE FIGURE MUST SUPPLY:

PANEL A — observable context or failure:
PANEL B — bottleneck or distinctive intervention:
PANEL C — bounded outcome or capability:

CONTROLLED FACTORS IN THE CONTRAST:
FACTORS THAT ARE NOT CONTROLLED:
VERIFIED NUMBER, IF ANY:
CAPTION FIRST SENTENCE:
DETAILS DEFERRED TO METHOD FIGURE:
```

Default to three panels or fewer. If the figure needs more, justify the extra branch by the question it answers.

## Draft the method-figure brief

```text
INPUTS:
OUTPUTS:
NOVELTY LOCATION:
PERSISTENT STATE:
TIME OR DEPTH AXIS:
REPEATED / SHARED MODULES:
TRAINABLE COMPONENTS:
FROZEN COMPONENTS:
PRIVILEGED TRAINING SIGNALS:
TRAINING-ONLY COMPONENTS:
INFERENCE-ONLY OR DEPLOYMENT PATH:
LOSSES AND THEIR TARGETS:
ARROW LEGEND:
WHAT IS INTENTIONALLY OMITTED:
```

Then perform a verbal trace from one input to one output. Every object and arrow that cannot be named in the trace is a candidate for removal.

## Build the claim-to-evidence matrix

| Priority | Claim | Hypothesis | Strongest alternative | Manipulation | Controls | Metric | Falsifier | Decision rule | Cost |
|---:|---|---|---|---|---|---|---|---|---|
| 1 |  |  |  |  |  |  |  |  |  |

Order rows by claim importance, then by information gain per unit cost. The main paper should contain the evidence for the highest-priority claims; appendix placement does not rescue a missing central test.

## Design the experiment ladder

```text
E0 — pipeline sanity
Question:
Expected observation:
Stop if:

E1 — cheapest discriminator
Alternative weakened:
Manipulated variable:
Controlled variables:
Decision rule:

E2 — matched main comparison
Baselines:
Tasks and metrics:
Tuning budget:
Seeds and uncertainty:

E3 — mechanism / ablation
Intermediate target:
Predicted directional change:
Falsifier:

E4 — boundary / robustness
Shift:
Expected success region:
Expected failure region:

E5 — cost / scaling confirmation
Resource axis:
Operating points:
Adoption threshold:
```

Skip any rung that cannot change the paper's conclusion.

## Run the reviewer attack

Ask the strongest version of each objection:

- Is the gain explained by more data, parameters, steps, tuning, or privileged information?
- Is the selected baseline weaker than the true closest alternative?
- Does the figure imply causality that the experiments do not identify?
- Does the mechanism predict an intermediate effect that was never measured?
- Are the examples or axes selected after seeing the result?
- Do variance, failures, or negative cases overturn the headline?
- Is the deployment cost merely shifted elsewhere?
- Does the method fail under a condition the introduction claims to solve?

For each objection, answer with `covered`, `partially covered`, `uncovered`, or `not applicable`, followed by exact evidence or the next test.

## Return the synthesis

Use this compact structure:

```markdown
# Design thesis

# What the corpus teaches
| Pattern | Similarities | Differences | Why | Strength | Weakness |

# Recommended teaser
Storyboard, visual grammar, and caption.

# Recommended method figure
Information hierarchy, flows, and legend.

# Experiment program
Prioritized claim-to-evidence matrix and stop rules.

# Verification and risks
Trusted evidence, unresolved confounds, and reviewer attacks.
```

Separate observed paper practices from recommendations. A popular pattern is not automatically a good pattern.
