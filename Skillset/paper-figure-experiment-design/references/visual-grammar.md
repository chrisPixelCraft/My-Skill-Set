# Visual Grammar for Research Figures

## Start from the communicative job

The same visual form can be excellent or misleading depending on its job. Select one primary job before choosing panels, icons, or colors.

| Figure 1 archetype | Use when | Minimal composition | Main advantage | Main failure risk |
|---|---|---|---|---|
| Failure diagnosis | A repeatable failure motivates the method | observed failure -> diagnostic evidence -> repair target | Makes necessity concrete | Implies causality from correlation |
| Paradigm contrast | One representational or procedural choice is central | prior approach vs proposed approach under matched context | Contribution is easy to locate | Bundles several changes into “ours” |
| Outcome first | A result is surprising and already trustworthy | one result plot plus a tiny mechanism cue | Immediate relevance | Cherry-picks or hides cost |
| Capability story | The contribution is best understood through behavior | real input -> intermediate behavior -> output | Concrete and memorable | Anecdote substitutes for evaluation |
| Benchmark taxonomy | The contribution defines what should be measured | orthogonal task axes plus representative examples | Establishes coverage | Taxonomy is decorative or overlapping |
| Causal question map | The paper studies mechanisms rather than a new model | variables -> interventions -> readouts -> research questions | Aligns paper structure | Too abstract for a cold reader |
| Data-to-deployment | Data construction or scaling is itself the contribution | sources -> representation -> training -> deployment evidence | Shows the full asset chain | Becomes an unreadable pipeline |

Do not combine archetypes unless both jobs remain legible. A teaser that is simultaneously a taxonomy, full architecture, training recipe, and results dashboard usually performs none of them well.

## Build the teaser

Use this sequence for a motivation-led paper:

```text
context -> observable failure -> diagnosed bottleneck -> proposed intervention -> bounded payoff
```

The figure may omit one stage, but the caption must recover it. When using an old-versus-new contrast, keep the input, task, model scale, and evaluation target visually matched. If multiple factors differ, name the comparison as a system-level bundle rather than a controlled mechanism.

Prefer these elements:

- one real or recognizable input;
- one visible failure or bottleneck;
- one highlighted intervention point;
- one output that demonstrates why the intervention matters;
- at most one verified headline number.

Use evidence badges such as `-32% latency` only when the underlying run is trusted and the comparison is fair. Otherwise describe the qualitative direction without a number.

## Use a stable reading order

Favor left-to-right for causal or procedural stories and top-to-bottom for hierarchy. Number panels when the path can be ambiguous. Put exceptions, optional paths, and training-only modules outside the dominant spine.

Use visual variables semantically:

- color identifies stable entity classes, not decoration;
- line style distinguishes flows only when the distinction matters;
- enclosure indicates scope or stage;
- repetition indicates recurrence or time;
- opacity indicates inactive, frozen, or unavailable components only when labeled;
- scale encodes magnitude only when the scale is meaningful.

Keep one legend across all paper figures. Do not reuse the same color for different concepts or different colors for the same concept.

## Design the motivation figure

A motivation figure must make the gap observable before it makes the method desirable.

For failure-based motivation, show three evidence layers:

1. **Phenomenon:** the failure occurs under a named condition.
2. **Localization:** a diagnostic narrows the likely bottleneck.
3. **Consequence:** the bottleneck damages the target behavior or metric.

Use a causal arrow only if an intervention supports it. With correlational evidence, use language such as “co-occurs with,” “is associated with,” or “suggests.” A proposed explanation can appear as a hypothesis, but must be visually marked as such.

Useful contrast pairs include:

```text
uniform vs progressive supervision
always-compute vs selective-compute
explicit bottleneck vs latent representation
outcome-only vs process guidance
short context vs memory-augmented context
single modality vs grounded multimodal state
```

The pair should expose the scientific variable, not merely brand the right panel as “ours.”

## Design the method figure

The reader should answer these questions in about 30 seconds:

- What enters and exits the system?
- Which state persists or changes?
- What repeats over time or depth?
- What is learned, frozen, or discarded?
- Where does supervision enter?
- What differs between training and inference?
- Which component embodies the claimed novelty?

Use three semantic layers:

1. **Interface layer:** task inputs, outputs, and external environment.
2. **Computation layer:** only the modules and state transitions needed to explain the method.
3. **Learning layer:** targets, losses, teachers, frozen modules, and gradient destinations.

Separate the learning layer below or beside the inference spine. If a decoder, teacher, simulator, or privileged modality disappears at inference, show the removal explicitly. If a component is shared across steps, draw it once with a recurrence marker unless separate copies have distinct parameters.

Name arrows when their semantics are not obvious:

```text
data / tokens
latent state
conditioning
control or routing
target or supervision
gradient
```

Avoid unlabeled bidirectional arrows. They commonly hide whether information is concatenated, cross-attended, distilled, optimized, or merely compared.

## Adapt to the paper genre

| Paper type | Figure 1 should foreground | Method figure should foreground | Common mistake |
|---|---|---|---|
| New model | bottleneck and intervention | state flow, supervision, train/inference | architecture dump |
| Training method | failure dynamics or supervision mismatch | targets, schedules, parameter updates | omitting the baseline training path |
| Inference method | compute allocation and outcome | control policy, stopping, reused state | hiding overhead |
| Benchmark | task axes and coverage | generation protocol and evaluation unit | showing model architecture instead of benchmark design |
| Interpretability | research questions and interventions | variables, interventions, readouts | treating a probe as causal evidence |
| Robotics or multimodal | task, physical state, and observable output | temporal rates, modalities, actions, privileged targets | tiny screenshots and no time axis |
| Scaling or systems | Pareto or scaling result | resource path and bottleneck | unmatched hardware or budget |

## Coordinate figures across the paper

Use progressive disclosure:

```text
Figure 1: why care and what changed
Figure 2: how the system works
Figure 3: whether the central claim holds
Figure 4+: why, where, and when it holds or fails
```

Do not repeat the same pipeline at three levels of detail unless each version answers a different question. Keep terminology, color, panel order, and entity icons stable across figures.

## Reject common anti-patterns

- **Spaghetti teaser:** too many modules obscure the thesis. Move implementation detail to the method figure.
- **Decorative old-versus-ours:** the panels differ cosmetically but do not expose a controlled variable.
- **Unverified causal arrow:** a diagnostic correlation is drawn as a mechanism.
- **Result collage:** several benchmarks are shown without a unifying question or matched scale.
- **Tiny text as documentation:** the figure is being used as a compressed methods section.
- **Rainbow semantics:** color changes by panel or encodes no stable category.
- **Training/inference blur:** privileged inputs or auxiliary modules appear deployment-ready.
- **Anecdotal success:** one attractive case is presented without selection criteria or failure cases.
- **Radar-chart theater:** axis choice, normalization, and area exaggerate weak or incomparable gains.

## Run the visual verification gate

Inspect the exported figure at the paper's final column width, not only on a large canvas.

- Five-second test: can a domain reader state the takeaway?
- Thirty-second trace: can they follow input to output and locate the novelty?
- Caption test: is the first sentence a claim and the rest sufficient to decode the figure?
- Grayscale test: do line styles, labels, and contrast preserve meaning?
- Occlusion test: if the title or “ours” label is hidden, does the evidence still reveal the point?
- Consistency test: do identical entities look identical across the paper?
- Honesty test: are uncertainty, omitted modules, and unmatched factors visible or disclosed?

Revise the information hierarchy before polishing aesthetics.
