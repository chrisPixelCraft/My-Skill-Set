---
name: paper-story-design
description: Design or audit research-paper teaser and motivation figures, method diagrams, and experiment suites by tracing claims to visual contrasts and identifiable evidence. Use when comparing figures across papers, planning a paper's visual narrative, translating a method into a diagram, or mapping claims to baselines, ablations, stress tests, diagnostics, and fair evaluations. Do not use for rendering final artwork alone.
---

# Paper Story Design

Treat a paper as an evidence-bearing visual argument, not a collection of attractive panels.

Use this invariant throughout:

```text
claim -> contrast or intervention -> visual encoding -> experiment -> decision
```

If any link is missing, label it as an evidence debt. Never let a figure imply a stronger claim than the experiment identifies.

## Choose the task mode

- `ANALYZE`: compare a paper corpus and extract transferable patterns.
- `DESIGN`: create a teaser, method-figure specification, and experiment suite for a paper.
- `AUDIT`: find narrative, diagram, and evidence gaps in an existing draft.

Use the smallest mode that answers the request. Respond in the user's language.

## Build the claim spine

Before designing anything, recover the paper's argument:

1. State both the candidate paper burden and the strongest wording currently defensible from available evidence. Their difference is evidence debt.
2. Split it into atomic claims. Mark each as performance, mechanism, generalization, efficiency, robustness, or scope.
3. For each claim, state the strongest alternative explanation.
4. Record the observation or intervention that would separate them.
5. Downgrade claims that cannot be identified with available evidence.

For a repository-backed design, identify the canonical active decision source before older drafts. List the primary method, deferred extensions, and explicit non-claims; never merge superseded designs into the current method.

Use this ledger:

| Claim | Strongest alternative | Discriminator | Required evidence | Status |
|---|---|---|---|---|
| Atomic, falsifiable claim | Simpler cause | Controlled contrast | Figure/table/test | supported / candidate / debt |

The teaser selects the central tension, the method figure exposes the proposed causal story, and the experiments pay the resulting evidence debts.

## Inspect precedents as evidence

When analyzing papers, inspect the actual figure, caption, surrounding introduction, method description, and relevant experiment—not captions alone.

For each useful precedent, record:

```text
role: teaser / motivation / method / result
message: one sentence
grammar: panel sequence and visual hierarchy
context: field, claim type, venue, page constraints
evidence link: figure/table/page or section
strength: what becomes easy to understand
risk: what may be hidden or overclaimed
transfer rule: when this pattern should be reused
```

Separate:

- `SOURCE FACT`: directly supported by the paper.
- `INFERENCE`: interpretation from cross-paper comparison.
- `HYPOTHESIS`: design idea that still needs testing.

Record the corpus inclusion rule, date range, field mix, missing figures, and source chain. Stop retrieving precedents when new papers no longer change the archetype set, strongest alternatives, or evidence obligations. Popularity, acceptance, and visual frequency are not evidence that a layout improves comprehension, impact, or acceptance.

Read [visual-story.md](references/visual-story.md) when selecting a teaser archetype or specifying a method diagram. Read [evidence-base.md](references/evidence-base.md) when precedent or empirical grounding matters.

## Design in three linked layers

### Teaser or motivation figure

Choose one dominant archetype based on the claim burden. Do not combine patterns unless each panel is indispensable.

The reader should recover in five seconds:

1. the problem or tension;
2. the proposed difference;
3. why that difference matters.

Prefer a visual causal contrast over a generic architecture overview. Use results in the teaser only when the comparison is fair, representative, and legible at column width.

### Method figure

Draw the executable scientific story:

- inputs, state, operations, outputs, and objectives;
- the novelty seam relative to the closest baseline;
- information, control, state, gradient, loss, and reward paths;
- train versus inference behavior;
- time, persistence, reset, and update scope;
- frozen, trainable, detached, oracle, or privileged components.

Every visible component must answer a claim, a reproducibility need, or an orientation need. Remove or de-emphasize decorative modules.

### Experiment suite

Convert each claim into a study, not an isolated run. Define the manipulated variable, controlled variables, inference unit, metrics, strongest baseline, uncertainty estimate, decision rule, and stop condition before execution.

Read [experiment-story.md](references/experiment-story.md) whenever proposing or auditing experiments.

## Apply the 7W interrogation

Interrogate the teaser, method, and experiments with `What, Why, How, Where, When, Who, Which`. These questions expose missing actors, locations, timescales, alternatives, and decisions that ordinary component lists miss.

Use the matrices and deliverable templates in [questions-and-templates.md](references/questions-and-templates.md).

## Verify independently

Run three explicit passes before trusting the design:

1. producer draft;
2. evidence verifier reconstructing the claim ceiling from sources;
3. visual verifier checking the artifact at final size.

Record material disagreements. A verbal “verified” assertion is not a pass.

Score every applicable gate as `PASS`, `CONDITIONAL`, `FAIL`, or `UNKNOWN`. The weakest load-bearing gate limits the final wording. Read [verifier-gates.md](references/verifier-gates.md) for corpus analysis, audits, result-bearing teasers, and mechanism claims.

### Visual verifier

- Can a reader state the message without the prose?
- Is the novelty visually dominant and the baseline visibly comparable?
- Does each color, shape, and arrow have one stable meaning?
- Are text, equations, and arrowheads readable at final size and in grayscale?
- Does the caption explain the claim, encoding, and panel order without repeating labels?
- Are symbolic details checked against the method rather than inferred from appearance?
- Are panels explicitly distinguishable as scope, method, evidence, diagnostic, or analogy?
- Are qualitative examples labeled all, random, representative, or success-only?

### Scientific verifier

- Does every headline claim have a matching experiment?
- Could tuning, data, compute, checkpoint choice, or evaluation protocol explain the gain?
- Does an ablation change only the claimed factor? If not, call it a system-dependence test.
- Are negative controls, simple alternatives, and relevant oracles included?
- Are exploratory and confirmatory results separated?
- Are uncertainty, failures, and boundary conditions visible?
- Do full tables or subgroups reverse the headline average?
- Are metric definition, denominator, evaluation unit, and checkpoint rule explicit?
- Do the abstract, teaser, body, tables, and limitations agree?

Do not trust a generated visual because it looks coherent. Semantic correctness and layout correctness are separate gates.

## Return decision-ready artifacts

Unless the user asks for a narrower result, return:

1. one-sentence paper burden;
2. claim ledger;
3. chosen teaser archetype, rejected alternatives, and tradeoff;
4. panel-by-panel storyboard or compact wireframe;
5. visual legend and caption draft;
6. method-diagram specification;
7. claim-to-experiment matrix;
8. gate report with the claim-strength ceiling;
9. risks, evidence debts, and remaining unknowns.

Do not render final artwork unless requested. Do not invent quantitative results, citations, or implementation details.
