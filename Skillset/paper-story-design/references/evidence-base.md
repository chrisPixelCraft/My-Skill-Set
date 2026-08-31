# Evidence base and scope

This skill was distilled from a VLA and embodied-AI corpus plus primary research on scientific figures and ML experimentation. Treat recurring patterns as design hypotheses, not universal laws.

## Corpus audit

The initial audit covered 83 locally curated papers across 14 families, including foundation VLAs, action policies, dual systems, adaptation, reinforcement learning, latent reasoning, world models, memory, retrieval, and benchmarks.

- Figure 1 text was recoverable for 65 of 83 papers.
- Figure 2 text was recoverable for 74 of 83 papers.
- Both were recoverable for 60 papers.
- Twenty-eight rendered pages from 15 deliberately varied papers were visually inspected by the primary pass.
- An independent generator pass inspected 24 papers across 13 families and 80 rendered PDF pages.
- Selected claims were checked against full PDF pages through alphaXiv.

This is broad within one research neighborhood but not an unbiased sample of all scientific fields. Caption coverage and author choices create selection bias. The skill therefore uses archetypes and verifier gates, not popularity counts.

The inventory is a convenience and citation-neighborhood sample, not a systematic review. Among 82 papers whose year could be parsed, 45 were from 2026 and 21 from 2025: 66 of 82, or 80.5%, came from 2025–2026. Survivorship, recency, author-style, and robotics/VLA domain bias prevent causal conclusions about which visual style improves comprehension or acceptance.

## Representative visual patterns

| Source | Observed design | Transferable lesson | Caution |
|---|---|---|---|
| [MemoryVLA, Fig. 1 p. 2](https://www.alphaxiv.org/abs/2508.19236) | temporal failure -> human-memory analogy -> method -> result | A teaser can compress motivation, mechanism, and payoff | Analogy can imply biology; four panels can overpack |
| [ChainVLA, Figs. 1–2 pp. 2–3](https://www.alphaxiv.org/abs/2608.02326) | query-boundary failure followed by a state lifecycle | Match teaser time logic to method time logic | Component removals bundle input, loss, and deployment effects |
| [RoboMME, Figs. 1–2](https://www.alphaxiv.org/abs/2603.04639) | task taxonomy, then representation × integration matrix | Benchmarks benefit from coverage first and controlled design second | Taxonomy does not itself establish discriminative validity |
| [RoboMME-Interference, Fig. 1 p. 2](https://www.alphaxiv.org/abs/2606.22338) | relevant session -> controlled distractors -> query | A minimal manipulation schematic can be the strongest motivation figure | Scope is narrow: nine tasks, one checkpoint per system |
| [ThinkAct, Fig. 1 p. 2](https://www.alphaxiv.org/abs/2507.16815) | capability montage around thinking and acting | Montages fit breadth claims and make behaviors concrete | Self-correction example also changes image input to video, so causality is ambiguous |
| [OpenVLA-OFT, Figs. 1–2 pp. 1–3](https://www.alphaxiv.org/abs/2502.19645) | deployment teaser, then three compact design-choice contrasts | Separate deployment motivation from recipe deltas | Best-checkpoint and unequal training-range choices constrain fairness |
| [AURA, Figs. 1 and 4](https://www.alphaxiv.org/abs/2606.02775) | minimal pipeline plus write-bandwidth Pareto curve | A simple technical story pairs well with explicit resource tradeoffs | Some studies have few seeds; efficiency axes are not wall-clock claims |
| [Anchor-Align, Figs. 1–2](https://www.alphaxiv.org/abs/2607.13429) | rollout failure/success followed by the method | Keep the teaser behavioral and the method diagram technical | Selected rollouts need aggregate and multi-seed support |
| [PearlVLA](https://www.alphaxiv.org/abs/2606.17924) | 2 × 2 design-space gap, then dense method | A missing quadrant can position a method precisely | Chosen axes may favor the proposed category |
| [VLA-ATTC](https://www.alphaxiv.org/abs/2605.01194) | result/Pareto-first teaser and alternative-inference comparison | Lead with the tradeoff when efficiency is the contribution | Pareto claims require matched axes and frontier baselines |

The figure and page pointers above are source facts. The lessons and cautions are cross-paper inferences.

## External figure research

### Method diagrams

[SciFig](https://www.alphaxiv.org/abs/2601.04390) separates planning, layout, rendering, and iterative refinement. Its evaluation decomposes figure quality into completeness/correctness, rubric content quality, perceptual design, and reference fidelity. Its documented errors show that layout refinement can leave semantic component errors untouched. Transfer these principles:

- plan structure before styling;
- preserve editability;
- evaluate technical accuracy separately from perceptual polish;
- verify equations, labels, and internal component structure against source text;
- use multiple diagnostic axes rather than one aesthetic score.

Scope: the benchmark is AI/ML-centered; teaser generalization is qualitative rather than systematically evaluated; some evaluation axes remain model-dependent.

### Graphical abstracts and teasers

[SciGA](https://www.alphaxiv.org/abs/2507.02212) treats first-page teasers as de facto graphical abstracts and finds strong field-dependent visual conventions. It frames reference choice using field match, semantic coherence, visual coherence, and aesthetic quality, with human validation. It also shows that multiple figures may plausibly serve as a paper's visual summary.

Transfer these principles:

- retrieve references by claim and domain, not only appearance;
- compare several plausible teaser designs;
- avoid assuming Figure 1 is optimal because of position;
- treat abstraction and visual appeal as insufficient without faithful meaning.

Scope: teaser labels are partly heuristic, the dataset is distributional rather than a causal test of design effectiveness, and graphical-abstract suitability is subjective.

### Text–graphic connection

[Graphing Inline](https://www.alphaxiv.org/abs/2603.10533) analyzes scientific graphics with a where–why–how framework and motivates tighter text–graphic correspondence through the split-attention problem. Its empirical object is word-scale graphics, not full method figures, so use the result only as support for explicit visual indexing and nearby explanatory links—not as direct proof of a teaser layout.

## Experiment-method evidence

[Best Practices for Machine Learning Experimentation](https://www.alphaxiv.org/abs/2511.21354) supports versioned preprocessing, simple baselines, consistent splits, train/test reporting, uncertainty across validation folds, learning curves, and structured experiment records. One recommendation to omit models that fail to learn is not adopted here: failed and invalid runs should be reported or quarantined with reasons because selective omission can bias the evidence.

The experiment rules in this skill are also constrained by the scientific tuning protocol: distinguish scientific, nuisance, fixed, and conditional variables; compare algorithms under comparable tuning opportunity; inspect curves and variance; separate discovery from confirmation; and charge complexity against demonstrated benefit.

## Limits of this evidence base

- Most audited examples are recent robotics and ML papers, many preprints.
- Author-reported experiments remain `CANDIDATE` unless independently reproduced.
- A visually common pattern may reflect venue convention rather than reader comprehension.
- Accepted or prominent papers cannot serve as a treatment/control study of figure design.
- Attractive figures can polish unsupported causal claims.
- New domains, venues, or media may require different visual grammar.

When these limits could change the recommendation, retrieve closer precedents and report the uncertainty instead of generalizing from this file.
