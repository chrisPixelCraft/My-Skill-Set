# Corpus Evidence and Distilled Patterns

## Audit scope

This reference records the evidence behind the skill's initial rules. It is a calibration set, not a universal law.

- Snapshot date: 2026-08-31.
- Corpus: 81 PDFs across 18 topic categories.
- Manifest: `/Users/chrishsieh/Documents/Survey-Ult/papers_by_category/MANIFEST.md`.
- Text extraction: Poppler `pdftotext -layout`; all 81 PDFs parsed successfully.
- Visual inspection: the first detected Figure 1 page for each paper and one heuristic method-figure candidate per paper were rendered into contact sheets and inspected.
- Context check: detailed local notes were inspected, and representative papers were queried through AlphaXiv for figure context, method structure, and claim-to-experiment links.

The method-figure selector was keyword-based, so some selected pages were results or title pages. Those false selections are themselves evidence that caption-only classification must remain `CANDIDATE` until a human or vision-capable model inspects the page.

## Corpus signals

The following are automated text-presence checks, not judgments of experimental quality.

| Signal in PDF text | Papers | Share |
|---|---:|---:|
| Explicit ablation language | 60 / 81 | 74% |
| Generalization, OOD, or unseen-condition language | 67 / 81 | 83% |
| Efficiency, latency, throughput, FLOPs, or inference-cost language | 77 / 81 | 95% |
| Seed, error-bar, standard-deviation, interval, or mean-plus-dispersion language | 39 / 81 | 48% |
| Scaling, sensitivity, hyperparameter, or sweep language | 79 / 81 | 98% |
| Causal, intervention, or counterfactual language | 39 / 81 | 48% |
| Qualitative, case-study, or failure-case language | 50 / 81 | 62% |
| Real-world or physical-robot language | 47 / 81 | 58% |

A loose text detector found a Figure 1 occurrence in 76 PDFs. Its first occurrence was on PDF page 1 in 37 papers, page 2 in 30, page 3 in 7, and page 4 in 2. The stricter caption inventory bundled with this skill recovered 74 captions and surfaced 7 papers for manual inspection. This supports early placement as a strong convention, not a rule that every paper must obey.

The gap between frequent efficiency or scaling claims and less frequent uncertainty language motivates an explicit reliability audit. Keyword presence can overcount incidental mentions and cannot establish whether a comparison is fair.

## Figure 1 archetypes observed

| Archetype | Representative papers | Shared design logic | Important variation |
|---|---|---|---|
| Failure diagnosis | SIM-CoT, Think-at-Hard, GTR | Show a concrete failure before naming the fix | Curves diagnose population behavior; examples diagnose semantic behavior |
| Paradigm contrast | LaST0, System-1.5, HyLaR | Put the old representational or execution bottleneck beside the proposed path | Some foreground latency; others foreground expressivity or routing |
| Method as teaser | Coconut, PonderLM, MolmoAct | Use a minimal pipeline when the mechanism is itself intuitive | Token models use schematic blocks; robotics adds real observations and outputs |
| Outcome first | Soft Thinking, PonderLM, Reasoning Palette | Lead with a performance, scaling, or efficiency frontier | Fast to understand but vulnerable to cherry-picking and budget mismatch |
| Capability story | MolmoAct, Hi Robot, LaST0 | Connect instruction, observation, intermediate state, and behavior | Qualitative examples are strongest when paired with a bounded quantitative claim |
| Benchmark taxonomy | RoboMME | Define orthogonal capability axes with one concrete task per axis | Coverage is persuasive only if the axes are nonredundant and operationalized |
| Causal question map | Dynamics Within Latent CoT | Turn research questions into variables, interventions, and readouts | High precision for experts, but needs plain-language framing for cold readers |
| Data-to-deployment | LDA-1B, Moto | Show how heterogeneous data acquire distinct roles before deployment | Easily becomes dense when dataset, model, objectives, and results share one panel |

## Method-figure patterns observed

The clearest diagrams repeatedly used these ideas:

- a dominant input-to-output spine with the novelty visually localized;
- repeated blocks or tokens to expose time, depth, or autoregressive order;
- stable color semantics for text, latent state, vision, action, teacher, and target;
- explicit stages for pretraining, post-training, and inference;
- icons or labels for frozen, trainable, shared, and removed-at-inference modules;
- a separate supervision path so that targets are not confused with inference inputs.

Dense diagrams became hard to audit when they mixed architecture, data construction, losses, training stages, examples, and results without hierarchy. Small fonts and unexplained arrows were more damaging than a lack of artistic polish.

## Experiment patterns observed

The corpus repeatedly separates evidence into complementary roles:

1. **Main comparison:** Does the full system improve the target metric against strong baselines?
2. **Efficiency frontier:** Is the gain retained at comparable token, latency, step, memory, or compute budgets?
3. **Component evidence:** Which module or supervision signal is necessary, and is a simpler replacement sufficient?
4. **Dose or scaling:** How does performance change with latent steps, recurrence, model size, data amount, or horizon?
5. **Mechanism evidence:** Does the proposed intervention change the claimed intermediate representation or behavior?
6. **Boundary evidence:** Does the effect persist under OOD tasks, new embodiments, occlusion, noise, longer horizons, or weaker teachers?
7. **Reliability evidence:** Are gains stable across seeds, checkpoints, environments, and training failures?

The strongest studies align the experiment sequence with the story sequence. A failure-first teaser is followed by a direct repair test; a selective-compute teaser is followed by quality-cost curves; a taxonomy teaser is followed by stratified evaluation across its axes.

## Representative AlphaXiv checks

These papers were used to verify that the visual reading matched the authors' surrounding text.

- [SIM-CoT](https://www.alphaxiv.org/abs/2509.20317v2): Figure 1 moves from training collapse to information loss, geometric drift, and semantic homogenization; Figure 2 locates the repair at step-level supervision. The later token-count ablation tests the condition that motivated the method.
- [SCOUT](https://www.alphaxiv.org/abs/2505.24181v1): Figure 1 contrasts uniform with progressive supervision; Figure 2 maps teacher strength to recursive reasoning stages. The visual claim is a curriculum mismatch, not merely a new block diagram.
- [Think-at-Hard](https://www.alphaxiv.org/abs/2511.08577v4): Figure 1 shows both correction and overthinking, which motivates selective rather than universal extra computation. Its experiments therefore need both accuracy and skipped-compute evidence.
- [Dynamics Within Latent CoT](https://www.alphaxiv.org/abs/2602.08783v3): Figure 1 is a research-question roadmap; Figure 2 operationalizes variables, interventions, propagation, and readouts. This is a useful template for analysis papers whose contribution is a protocol.
- [LaST0](https://www.alphaxiv.org/abs/2601.05248v4): Figure 1 contrasts explicit linguistic or visual reasoning with latent spatio-temporal reasoning; Figure 2 exposes slow reasoning and fast action rates plus privileged latent targets. The frequency distinction is part of the scientific claim.
- [RoboMME](https://www.alphaxiv.org/abs/2603.04639v3): Figure 1 defines temporal, spatial, object, and procedural memory through concrete tasks; Figure 2 crosses memory representations with integration mechanisms. Taxonomy and system design remain separate.
- [LDA-1B](https://www.alphaxiv.org/abs/2602.12215v2): heterogeneous data are assigned different learning roles, then connected to a scalable latent dynamics model. The experiment program must isolate data quality, objective, scale, and task horizon.
- [GTR](https://www.alphaxiv.org/abs/2503.08525v2): Figure 1 uses a sequential failure case to make thought collapse visible; larger-model and longer-training checks weaken the simple capacity or budget explanation before process guidance is proposed.
- [MolmoAct](https://www.alphaxiv.org/abs/2508.07917v4): Figure 1 uses decodable depth, trajectory, and action outputs to explain grounded action reasoning; Figure 2 separates pretraining from post-training and inference.
- [PonderLM](https://www.alphaxiv.org/abs/2505.20674v3): a compact recurrent embedding update serves as the method overview, while scaling curves support the claim that additional continuous computation is a distinct scaling axis.

## Distilled causal explanation

These patterns work because a research reader is solving three search problems:

```text
Where is the novelty?
Why should it matter?
Which evidence permits the stated conclusion?
```

A good teaser reduces the first two searches. A good method figure makes the intervention and information flow inspectable. A good experiment program closes the third search while exposing where the conclusion stops.

The recurring old-versus-new composition is effective because it compresses a counterfactual. Its weakness is the same: if more than one factor changes, the counterfactual is not identified. The recurring pipeline is effective because it externalizes state and time. Its weakness is that implementation completeness competes with conceptual clarity. The recurring result-first teaser is effective because it establishes stakes immediately. Its weakness is that the reader cannot judge fairness without the hidden protocol.

## Boundary of this evidence

The corpus is concentrated in latent reasoning, multimodal reasoning, and embodied AI. The visual grammar is likely transferable to adjacent AI/ML work, but domain-specific conventions may differ in theory, human-subjects research, hardware, biology, or purely systems papers. Several papers are preprints and may change across versions. Re-audit the target venue and closest papers before treating any stylistic pattern as canonical.
