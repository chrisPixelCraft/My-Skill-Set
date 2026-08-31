# Verifier gates and stop rules

Use these gates before turning a precedent into a rule, a visual into a claim, or a result into a conclusion.

Score each applicable gate:

- `PASS`: evidence supports the intended use.
- `CONDITIONAL`: usable only with an explicit scope or caveat.
- `FAIL`: the artifact cannot support the intended claim.
- `UNKNOWN`: required evidence was not found.

The weakest load-bearing gate sets the claim-strength ceiling.

## Fourteen gates

1. **Corpus** — Record inclusion rule, source chain, date range, fields, missingness, and sampling bias. Convenience samples yield domain-local candidate rules only.
2. **Primary context** — Cite paper, PDF page, figure, table, or section. Inspect the visual, caption, nearby prose, relevant methods/results, and appendix. Caption-only analysis fails.
3. **Role and traceability** — Label every panel as scope, method, evidence, diagnostic, or analogy. Trace every arrow, number, and causal verb to a source or hypothesis.
4. **Result leakage** — Do not design the method story backward from a winning result. A result-bearing teaser must keep its estimand and scope visible and cannot use performance as mechanism proof.
5. **Selection** — State whether cases are all, random, prespecified representative, post-hoc representative, or success-only. Check complete results and failure cases.
6. **Estimand** — Verify metric definition, binary versus partial credit, denominator, macro versus micro average, evaluation unit, and paired initial conditions.
7. **Baseline fairness** — Compare data, pretraining, input modality, backbone, output or action space, training compute, online interaction, and evaluation protocol.
8. **Tuning and checkpoint** — Compare search ranges, budgets, boundary hits, per-method retuning, checkpoint selection, validation/test access, and winner's curse.
9. **Uncertainty** — Separate retraining variance from evaluation-episode variance. Fixed evaluation seeds and many episodes from one checkpoint do not estimate training variance.
10. **Mechanism** — Predeclare the strongest alternative and falsifier. Without a discriminating intervention, negative control, or rescue, use “consistent with,” not mechanism language.
11. **Heterogeneity and transport** — Inspect the complete subgroup grid, direction reversals, and domain boundaries. One robot, simulator, backbone, or task family does not justify universal wording.
12. **Internal consistency** — Compare abstract, teaser, body claims, full tables, appendix, and limitations. A contradictory full table blocks the broader claim.
13. **Legibility** — Render at final column or page size. Small text, dense panels, decorative montages, and hidden conditions fail even if the source canvas is clear.
14. **Trust state** — Label evidence as reproduced, author-reported, cross-paper, selected qualitative, failed, or unknown. Only independently verified evidence is trusted for a new empirical claim.

## Claim-language ladder

Use the strongest phrase the gates permit, never the most persuasive phrase available.

| Evidence | Maximum wording |
|---|---|
| Selected qualitative example | “illustrates” |
| Observational association | “is associated with” |
| Component removal | “is useful or necessary in the tested configuration” |
| Targeted intervention with controls | “supports a causal role” |
| Discriminating intervention replicated across settings | bounded mechanism claim |

Attention, retrieval maps, latent projections, smooth trajectories, and probes are diagnostics. They create or refine hypotheses; they do not alone establish semantic use or mechanism.

## Stop or downgrade when

- Only a caption, schematic, or qualitative case is available: keep the rule `CANDIDATE`.
- Baseline, tuning, or checkpoint fairness is unresolved: stop at descriptive observation.
- A credible subgroup reverses direction: replace universal wording with a conditional claim.
- A full table contradicts the prose, or two credible counterexamples defeat a rule: do not promote it as a general rule.
- The strongest alternative has no discriminating test: use “consistent with.”
- Training variance is absent and the effect may fit plausible instability: label exploratory.
- Evidence comes only from robotics/VLA: do not transport the convention to all ML or science.
- A new paper no longer changes the boundary, alternatives, or evidence matrix: stop retrieval.
- A visual element resolves no uncertainty about scope, intervention, estimand, or uncertainty: remove it.

For an empirical design rule to move beyond a local hypothesis, require at least three independent works across at least two task or method families plus a deliberate counterexample search. This is a verifier heuristic, not a statistical law.
