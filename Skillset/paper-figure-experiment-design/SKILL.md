---
name: paper-figure-experiment-design
description: Audit or design AI/ML paper methods, teaser and motivation figures, method diagrams, and claim-testing experiments. Use for cross-paper pattern distillation, research-method design, figure storyboards or critiques, and experiment matrices. Do not use for generic literature summaries, slide decks, or final raster/vector rendering.
---

# Paper Figure and Experiment Design

Treat the paper's figures and experiments as one claim system:

```text
problem -> gap -> intervention -> evidence -> boundary
```

A visually attractive figure is not enough. Every visual choice must help the reader recover this chain, and every load-bearing arrow must have an experiment behind it.

## Route the task

- For a paper-corpus audit, inventory captions first, then inspect the rendered pages. Use `scripts/inventory_paper_figures.py` for the inventory and read `references/corpus-evidence.md` for the evidence standard.
- For designing the scientific method itself, read `references/method-design.md`.
- For teaser, motivation, or method figures, read `references/visual-grammar.md`.
- For experiments, ablations, baselines, or result plots, read `references/experiment-design.md`.
- For a full audit or design brief, also read `references/5w2h-templates.md`.

Use only the references needed for the request.

## Establish the research object

Before drawing or proposing experiments, write five one-sentence statements:

1. **Problem:** What observable situation matters?
2. **Gap:** What specifically fails in the strongest relevant alternative?
3. **Intervention:** What one change is scientifically distinctive?
4. **Claim:** What outcome should change, under which conditions?
5. **Boundary:** Where should the claim stop?

If these sentences cannot be made mutually consistent, pause figure design and repair the research story. Do not use visual polish to hide an unidentified contribution.

## Build an evidence packet

For each source paper, collect:

- figure number, PDF page, caption, and the paragraph that introduces it;
- the main method figure and its surrounding method text;
- the experiments, ablations, limitations, and appendix details tied to the figure's claim;
- provenance: paper title, version, source, and access date.

Prefer local PDFs when supplied. Use AlphaXiv PDF queries when available to recover figure context and claim-to-experiment links. Render and inspect the actual page: captions reveal stated intent, but not hierarchy, density, legibility, or misleading visual emphasis.

Label every extracted statement as one of:

- `FACT`: explicit in the paper;
- `INFERENCE`: supported interpretation;
- `DESIGN CHOICE`: recommendation for the target paper;
- `UNKNOWN`: missing or unresolved.

Do not turn an author's explanation into verified causality. Do not treat a summary note as ground truth when the PDF is available.

## Audit a corpus

Sample for distinct communicative strategies, not paper count alone. Maintain a pattern map with:

```text
paper | figure job | visual grammar | claim | evidence | advantage | failure risk
```

Cluster figures by job before comparing aesthetics. Stop reading more papers when new examples no longer change the archetypes, failure modes, or design decision. Record exceptions that challenge the current rule.

## Design the figures

Choose exactly one primary job for Figure 1:

```text
motivate a failure
compare paradigms
show the headline outcome
demonstrate a capability
define a task taxonomy
state the causal question
```

Then draft the caption before drawing. The first caption sentence must state the intended takeaway. Use the smallest visual structure that makes the comparison identifiable.

For the method figure, expose:

```text
input -> state transformations -> output
                 ^
          supervision / loss
```

Mark time, train versus inference, trainable versus frozen, repeated modules, and removed-at-inference components explicitly. Distinguish data flow, state reuse, control, and gradient or supervision with different arrow styles only when all are necessary.

## Design the method

Translate the diagnosed gap into a minimal intervention chain:

```text
observed failure -> cause hypothesis -> target variable -> intervention
-> predicted intermediate change -> predicted task outcome -> boundary
```

Choose one primary novelty class: representation, computation schedule, supervision, objective, memory, routing, data use, or task interface. Treat supporting modules as engineering unless they carry an independently tested hypothesis. Prefer an intervention at the narrowest seam that can change the target variable.

Before adding a component, name its unique role, simpler replacement, new cost, likely failure mode, and falsifying result. If these cannot be named, remove or postpone it.

## Design the experiments

Create a claim-to-evidence matrix before scheduling runs. Each claim needs:

```text
hypothesis | prediction | strongest alternative | decisive comparison | falsifier | decision rule
```

Classify variables as `scientific`, `nuisance`, `fixed`, or `conditional`. Match data, backbone, training budget, inference budget, evaluation protocol, and tuning effort unless one is the manipulated variable. Pay the complexity tax with component ablations, compute-matched baselines, reliability evidence, and an explicit cost accounting.

Run the cheapest discriminating experiment first. A full benchmark suite is not a substitute for a causal or component-level test, and an ablation is not informative if it changes several mechanisms at once.

## Verify before trusting

Use three gates:

1. **Visual:** A domain reader can state the takeaway after five seconds; text remains legible at final size; grayscale does not destroy meaning; arrows and colors have consistent semantics.
2. **Scientific:** Every load-bearing visual claim maps to evidence; comparisons isolate the claimed variable; uncertainty and failure cases are not hidden.
3. **Narrative:** Figure 1, method figure, results, and abstract make the same bounded claim without changing terminology.

Artifacts are `CANDIDATE` until all applicable gates pass. Keep failed or ambiguous runs out of figures and conclusions.

## Return a decision-ready package

Unless the user asks for a smaller output, return:

1. a one-sentence design thesis;
2. a pattern map with similarities and differences;
3. a method-design rationale from failure to intervention;
4. a teaser storyboard and self-contained caption draft;
5. a method-figure storyboard and legend;
6. a prioritized claim-to-evidence experiment matrix;
7. advantages, disadvantages, and likely reviewer attacks;
8. remaining uncertainty and the next highest-information action.

Keep facts separate from recommendations. Prefer one defensible figure concept and one coherent experiment program over many interchangeable options.
