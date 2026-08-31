# Visual story grammar

Use this reference to select a visual argument, not to imitate surface style.

## Teaser archetypes

| Archetype | Narrative grammar | Best fit | Strength | Main risk |
|---|---|---|---|---|
| Failure to remedy | failure -> cause -> intervention -> outcome | A concrete failure motivates a mechanism | Fast causal story | Anecdotal or cherry-picked failure |
| Contrast ladder | incumbent A -> incumbent B -> proposed delta | A representation or inference paradigm changes | Difference is easy to locate | Weak or straw-person incumbents |
| Old versus new | shared pipeline -> missing property -> local delta | A small, precise design change | Novelty is easy to locate | Hides dependencies shared by both sides |
| Temporal boundary | earlier cue -> information loss -> later query -> rescue | Memory, streaming, or delayed-credit work | Makes time and state visible | Timeline can imply causality without controls |
| Design-space map | two axes -> occupied cells -> missing quadrant | Contribution fills an identifiable gap | Systematic positioning | Axes may be non-orthogonal or self-serving |
| Taxonomy montage | task families or failure classes around a hub | Benchmark or broad capability paper | Communicates scope | Breadth replaces a sharp claim |
| Study-axis map | research questions -> controlled axes -> findings | Empirical or benchmark study | Makes the paper's logic explicit | Arbitrary axes can manufacture coherence |
| Capability montage | diverse before/after examples | Generalist or emergent behavior paper | Concrete and memorable | Qualitative selection bias |
| Qualitative + quantitative | behavior example beside aggregate result | Behavior and performance jointly matter | Connects meaning to magnitude | Numbers become unreadable or decorate cherry-picked cases |
| Result first | headline curve, table, or Pareto frontier -> method cue | Quantitative gain or tradeoff is the contribution | Immediate impact | Unfair axes, hidden variance, or cherry-picking |
| One-picture pipeline | input -> novelty -> output, minimal text | Mechanism is simple and visual | Low cognitive load | Omits training or boundary conditions |

Choose the archetype whose failure mode is easiest to control for this paper. A hybrid teaser should still have one dominant reading order.

## Teaser construction

1. Write the five-second message in one sentence.
2. Choose the smallest contrast that makes the message visible.
3. Assign one job to each panel: context, failure, delta, consequence, or evidence.
4. Order panels by the reader's inference, not the implementation chronology.
5. Put the visual climax on the proposed difference or decisive result.
6. Move supporting detail to the method figure or caption.
7. Give every panel one epistemic role: `scope`, `method`, `evidence`, `diagnostic`, or `analogy`.

A useful caption has four clauses:

```text
Context. Failure or gap. Proposed contrast. Supported consequence and scope.
```

Do not write an unqualified causal verb such as “enables” when the figure only shows correlation or selected examples.

If using a rollout or case study, disclose whether it is all, random, representative by a declared rule, or success-only. Pair it with aggregate evidence and visible failures. If using a result, show the estimand, absolute value, denominator or uncertainty, comparison scope, and any important subgroup reversal.

## Method-diagram grammar

### Establish the skeleton

- Use a left-to-right main path unless time, hierarchy, or feedback requires another layout.
- Place the closest baseline path beside the proposed delta when novelty is local.
- Separate training and inference into bands or panels.
- Separate multiple stages with stable tokens, colors, and labels.
- For temporal methods, show the state lifecycle: read, update, write, retain, reset.
- For hierarchy, show ownership and cadence at each level.
- Keep the overview to the method contract; move internals to a detail figure when necessary.

### Encode semantics consistently

Use one visual meaning per channel:

- solid arrow: primary forward information flow;
- dashed arrow: supervision, loss, reward, or optional path;
- loop arrow: recurrence or update, with cadence;
- color: role or state, not arbitrary decoration;
- outline or fill: trainable, frozen, oracle, or selected state;
- panel boundary: phase, scope, or timescale.

Add a legend when a reader could plausibly assign another meaning. Never encode the same distinction with color alone.

### Expose hidden scientific details

Make these explicit when relevant:

- tensor, token, or representation type and dimensional bottleneck;
- information source and legal availability;
- privileged labels or oracle paths;
- gradient stopping and parameter sharing;
- update frequency, write budget, and memory capacity;
- within-call, cross-step, cross-episode, or cross-task persistence;
- reset boundary and failure fallback;
- training-only modules removed at inference;
- action or output granularity.

These details often determine whether an experiment is fair or a claim is identifiable. If removing block names leaves only “encoder -> transformer -> decoder,” the diagram is not carrying enough method-specific information.

## Context determines form

- A benchmark teaser should foreground coverage and discriminative task structure, not a model block diagram.
- A mechanism paper should foreground a controlled failure and the intervention that repairs it.
- A systems or efficiency paper should foreground throughput, latency, memory, or Pareto axes with matched-quality baselines.
- A generalist model may need a capability montage, but representative sampling and quantitative backing remain mandatory.
- A small architectural delta benefits from baseline-aligned comparison; a new paradigm benefits from a lifecycle or design-space view.

Do not transfer a computer-vision or robotics figure convention blindly across domains. Field match, semantic match, and claim match are separate dimensions.

## Failure modes and repairs

| Failure | Why it fails | Repair |
|---|---|---|
| Architecture dump as teaser | Shows machinery before motivation | Replace modules with the central contrast |
| Human-brain analogy | Intuitive but may imply false mechanism | Label it analogy; pair it with the actual computation |
| Too many panels | No dominant inference path | Keep one claim; demote supporting panels |
| Colored spaghetti | Relations are not typed | Reduce paths; define arrow hierarchy and legend |
| Tiny equations | Completeness destroys legibility | Show operation names; move formulas to text |
| Result badge without protocol | Number looks authoritative but is unauditable | Name baseline, metric, scope, and uncertainty |
| Before/after cherry-pick | Selected examples imply generality | Declare selection rule; pair with aggregate evidence |
| Average hides reversals | A global mean implies uniform gains | Inspect and expose decisive per-task or per-suite effects |
| Omnibus method figure | Training, inference, data, and results compete | Split phases; keep shared visual identity |
| Decorative module | Figure suggests importance without evidence | Remove, gray, or add the corresponding test |

## Figure quality gates

Evaluate semantic and perceptual quality separately.

### Semantic gate

- complete key components;
- correct relations and direction;
- faithful symbols, equations, and labels;
- recoverable novelty and scope;
- no implied unsupported result.

### Perceptual gate

- clear hierarchy and reading order;
- balanced density and whitespace;
- aligned components and unambiguous arrows;
- consistent typography;
- accessible contrast and redundant encodings;
- readable at final single- or double-column size.

Iterative layout review can fix overlap and routing but may not catch a wrong equation, missing graph node, or mislabeled variable. Verify those against source text independently.
