# Experiment Templates

## Contents

1. Next-round experiment plan
2. Method comparison plan
3. Result review
4. Adoption decision
5. Failure diagnosis report
6. Minimal experiment log
7. Paper-claim evidence table

## 1. Next-round experiment plan

```markdown
# Experiment: <name>

## Question
<One narrow, decision-relevant question>

## Why this question now
<What uncertainty or bottleneck it resolves>

## Incumbent
- Model/config:
- Best known metric:
- Training budget:
- Code/config reference:

## Hypothesis
<Expected direction and mechanism, stated without assuming it is true>

## Variables
| Role | Variable | Values/range | Reason |
|---|---|---|---|
| Scientific | | | |
| Nuisance | | | |
| Fixed | | | |
| Conditional | | | |

## Fairness requirements
- Baseline tuning:
- Candidate tuning:
- Equal budget rules:
- Checkpoint rule:
- Evaluation rule:

## Study
- Trials per scientific setting:
- Search algorithm:
- Search spaces:
- Seeds/repeats:
- max_train_steps:
- Evaluation cadence:
- Checkpoint cadence:

## Budget
- GPUs/devices:
- Estimated GPU-hours:
- Parallelism:
- Deadline:

## Required diagnostics
- Training/validation curves
- Hyperparameter-axis plots
- Search-boundary check
- Best-checkpoint step distribution
- Failure-trial inspection

## Decision rule
ADOPT if:
REJECT if:
HOLD if:

## Caveats
<What fixed choices limit the conclusion>

## Next branch
- If positive:
- If negative:
- If ambiguous:
```

## 2. Method comparison plan

```markdown
# Comparison: <A> vs <B>

## Scientific claim
<Exactly what comparison is intended to establish>

## Scientific variable
method ∈ {A, B}

## Conditional nuisance variables
### A
- learning rate:
- regularization:
- method-specific parameters:

### B
- learning rate:
- regularization:
- method-specific parameters:

## Shared fixed variables
- dataset/split:
- model scale if intentionally fixed:
- evaluation:
- training compute or step budget:

## Fairness audit
- Comparable search budget? yes/no
- Comparable search-space quality? yes/no
- Comparable checkpoint selection? yes/no
- Comparable evaluation? yes/no
- Same claim under fixed compute vs best achievable? specify

## Analysis
For each method:
1. optimize nuisance variables;
2. select best trial using same rule;
3. repeat best configuration to estimate retrain variance;
4. inspect curves;
5. compare performance and resource/complexity cost.
```

## 3. Result review

```markdown
# Result Review: <study>

## Conclusion
ADOPT / REJECT / HOLD

## What the study actually tested
<One sentence>

## Best results
| Condition | Best metric | Best config | Seed | Best step |
|---|---:|---|---:|---:|

## Search adequacy
- Top result on boundary?
- Enough nuisance coverage?
- Enough density?
- Invalid/failing regions?

## Curve diagnosis
- Overfitting:
- Still improving at end:
- Saturated early:
- Instability:
- Suspicious artifacts:

## Variance
- Retrain variance:
- Search variance:
- Data/eval variance:

## Fairness
- Baseline equally tuned?
- Same checkpoint rule?
- Same evaluation?
- Same budget semantics?

## Complexity delta
- Code:
- Hyperparameters:
- Compute:
- Memory:
- Inference:

## Evidence-supported claim
<What can be claimed safely>

## Unsupported stronger claim
<What the data do not establish>

## Next experiment
<Smallest resolving study>
```

## 4. Adoption decision

```markdown
# Adoption Decision

Candidate: <change>
Incumbent: <baseline>
Decision: ADOPT / REJECT / HOLD

## Evidence
- Performance delta:
- Repeatability:
- Search fairness:
- Curve health:

## Cost
- Training:
- Inference:
- Memory:
- Engineering complexity:
- Additional tuning dimensions:

## Caveats
- Fixed variables:
- Unresolved variance:
- Domain limits:

## Reason
<2-5 concise sentences>
```

## 5. Failure diagnosis report

```markdown
# Failure Diagnosis

## Symptom
<Observable failure>

## First failing point
<Step/run/commit where behavior changes>

## Ranked hypotheses
| Rank | Hypothesis | Evidence for | Evidence against | Test |
|---:|---|---|---|---|

## Measurement sanity
- Metric checked:
- Eval checked:
- Split/leakage checked:

## Training sanity
- LR/schedule:
- Gradient norm:
- Loss/activation anomalies:
- Precision:

## Systems sanity
- Throughput:
- Input stalls:
- Multi-host synchronization:

## Smallest discriminating test
<One experiment>

## Current status
BUG / CONFIG / SEARCH / BUDGET / OVERFIT / INSTABILITY / METHOD / UNKNOWN
```

## 6. Minimal experiment log

```markdown
- Study:
- Question:
- Date:
- Git commit:
- Config:
- Dataset version:
- Command:
- Hardware:
- Trials:
- Seeds:
- Training steps:
- Eval cadence:
- Best metric:
- Best checkpoint:
- Key plots:
- Known failures:
- Decision:
- Why:
- Next action:
```

## 7. Paper-claim evidence table

```markdown
| Claim | Necessary comparison | Nuisance controls | Evidence | Variance check | Caveat | Status |
|---|---|---|---|---|---|---|
| | | | | | | supported / weak / unsupported |
```

Use this table when turning experimental results into paper claims. Every claim should have a corresponding comparison and an explicit caveat if fixed choices restrict generality.
