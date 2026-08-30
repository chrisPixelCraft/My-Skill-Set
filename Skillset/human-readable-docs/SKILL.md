---
name: human-readable-docs
description: Rewrite or create human-facing Markdown, README files, research notes, experiment reports, benchmark summaries, design docs, and documentation so they are easy to scan and read. Use when Codex is writing or editing prose-heavy files, tables, findings, limitations, or structured notes. Enforce shallow hierarchy, concise but complete bullets, readable table cells, and removal of AI-style prose. Do not apply these formatting constraints to source code, JSON, YAML, logs, schemas, or machine-readable output unless the user explicitly asks.
metadata:
  version: "1.0.0"
---

# Human-Readable Documentation

Write documents for a human reader, not as an AI reasoning dump.

Priority:

**Readable → Scannable → Complete → Dense**

Preserve important facts. Simplify presentation instead of deleting necessary information.

## Structure

Keep document hierarchy shallow.

- Prefer `# → ##`.
- Use `###` only when needed.
- Avoid `####` or deeper.
- Merge closely related sections.
- Do not create headings for tiny ideas.

Each section should answer one clear question and show its conclusion early.

Use this flow when useful:

`Conclusion → Evidence → Limitation → Impact`

Do not mechanically create every stage when it adds no value.

## Bullet rules

Bullets must be concise **and semantically complete**.

A bullet must communicate a real fact, judgment, relation, or consequence. Do not reduce bullets to isolated keywords.

### Hard constraints

- Maximum list depth: **2 levels**.
- Default sibling bullets: **≤6**.
- Exceed 6 only when separate facts truly cannot be merged or regrouped without losing clarity.
- Human-language explanation in each bullet: **≤10 Chinese characters when writing Chinese**.
- Technical names, code identifiers, filenames, numbers, equations, and unavoidable English terms do not count toward the 10-character limit.
- Never fit multiple independent facts into one bullet just to reduce bullet count.
- If a point exceeds the limit, split it into a second-level bullet or another nearby bullet.

### Bullet quality

Bad — keyword only:

```markdown
- **限制:** proxy
- **用途:** timing
```

Bad — overloaded:

```markdown
- RoboMME 的 boundary 來自 planner，只能監督事件時間，也可能漏答案，因此主方法需要 mask。
```

Good:

```markdown
- Boundary 來自 planner
  - 只監督事件時間
  - 不能當完整 reward
- Subgoal 可能漏答案
  - 主方法需要 mask
```

The goal is not the shortest possible bullet. The goal is the shortest bullet that still carries a complete meaning.

## Atomic information

One bullet should express one main idea.

Split independent claims:

```markdown
- 新版包含 90 tasks
- 新舊 schema 不一致
- 實驗需固定版本
```

Use second-level bullets when facts have a parent-child relation:

```markdown
- 新舊 schema 不一致
  - 實驗需固定版本
```

Do not create artificial label/value fragments when a natural short statement is clearer.

Prefer:

```markdown
- Boundary 來自 planner
```

Over:

```markdown
- **來源:** planner
```

Keyword-first formatting is allowed only when it improves comparison or scanning and the remaining text still forms a meaningful statement.

## Tables

Tables are for comparison, not paragraph compression.

Every table cell follows the same bullet rules:

- Use bullets when a cell contains multiple facts.
- Allow at most 2 bullet levels.
- Keep each bullet concise and complete.
- Default to ≤6 sibling bullets.
- Do not place prose paragraphs inside cells.
- Do not chain many clauses with commas or semicolons.

Preferred conceptual form:

```markdown
| Benchmark | Important limits |
|---|---|
| RoboMME | • Boundary 來自 planner<br>  ↳ 只監督事件時間<br>• Subgoal 可能漏答案 |
```

If the Markdown renderer supports nested lists inside table cells, use real nested lists. Otherwise use `•` for first-level items and `↳` for second-level items so the rendered table remains visually hierarchical.

If a table cell becomes tall or explanation-heavy, keep only comparison-critical facts in the table and move detailed reasoning below it.

## Benchmark and research summaries

Never write an entire benchmark description as one bullet.

Decompose information by meaning, for example:

- dataset/schema
- annotation source
- reward or boundary
- intended use
- limitation
- risk
- version requirement

Do not force every benchmark to use every field. Include only relevant facts.

Preferred:

```markdown
### RoboMME

- Boundary 來自 planner
  - 只監督事件時間
  - 不代表完整 reward
- Subgoal 可能漏答案
  - 主方法需要 mask
```

Avoid:

```markdown
- RoboMME: is_subgoal_boundary 是 planner subtask boundary，只能監督 event timing，simple_subgoal、grounded_subgoal、choice_action 和 waypoint 又可能漏掉答案，因此主方法需要 mask。
```

## Writing style

Use direct technical language.

Prefer concrete statements:

> 相鄰 frame 過於相似，因此 latent 容易 collapse。

Avoid generic AI prose such as:

- It is worth noting that
- This highlights the importance of
- From a broader perspective
- There are several key considerations
- It should be emphasized that
- As mentioned previously
- This section aims to

Delete repeated conclusions, obvious statements, generic introductions, and meta-commentary that do not help the reader.

## Paragraphs vs bullets

Use paragraphs for reasoning that needs continuity:

- mechanism
- causal explanation
- interpretation
- argument

Use bullets for parallel information:

- findings
- limitations
- comparisons
- requirements
- decisions
- next steps

Do not turn the entire document into bullets.

Do not turn reasoning into nested bullet trees.

## Tables vs prose

Use a table when the reader needs to compare the same dimensions across several items.

Do not use a table merely to compress text.

If rows need long explanations, use:

1. a small comparison table;
2. short sections below for details.

## Preserve technical fidelity

Readability must not destroy correctness.

Preserve:

- important numbers
- experimental conditions
- dataset versions
- code identifiers
- filenames
- links and citations
- caveats that change interpretation

If simplification would make a statement misleading, keep the necessary qualification but restructure it into shorter bullets or prose.

## Evidence-Backed Reasoning

Do not compress away the rationale behind important conclusions.

For every non-trivial:
- conclusion
- design decision
- research gap
- experiment proposal
- interpretation

preserve:

**Evidence → Interpretation → Conclusion**

Evidence should be traceable to the original source:

- Code: `path:Lx-Ly`, function/class
- Document: file + section + line
- Paper: section / figure / table / equation
- Experiment: metric / run / artifact

Clearly label:

- **Fact** — directly supported by source
- **Inference** — derived from evidence
- **Hypothesis** — requires validation

When useful, write:

**Evidence:**\
**Interpretation:**\
**Conclusion:**\
**Uncertainty:**

Never remove reasoning evidence merely to make the document shorter.
Prefer concise but traceable explanations over unsupported summaries.

If evidence cannot be found, explicitly write:
`Evidence not found`.

Do not reproduce hidden chain-of-thought.
Instead provide enough source evidence and rationale for a human
to independently reconstruct and verify the conclusion.

## Final readability pass

Before saving a human-facing document, perform one cleanup pass.

Check:

1. Can the main point be found quickly?
2. Is any heading unnecessary?
3. Is hierarchy deeper than needed?
4. Does any bullet contain multiple independent facts?
5. Is any bullet only a keyword without meaning?
6. Is each Chinese bullet explanation within 10 characters, excluding technical tokens?
7. Does any list exceed 6 siblings without a real need?
8. Does any table cell hide a paragraph?
9. Can long table content move below the table?
10. Does any sentence sound like generic AI prose?
11. Important conclusions include traceable evidence and rationale.

Rewrite until the answer is easy to scan without losing important information.

## Final rule

When information is too dense:

> **Split it; do not cram it.**

When shortening would remove meaning:

> **Keep the meaning; restructure it.**
