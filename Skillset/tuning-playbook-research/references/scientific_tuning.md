# Scientific Tuning and Experiment Design

## Contents

1. Incremental tuning strategy
2. Exploration versus exploitation
3. Choosing one experimental goal
4. Variable roles
5. Conditional hyperparameters
6. Building studies
7. Allocating trial budget
8. Search-space design
9. Sampling/search algorithms
10. Analyzing study results
11. Hyperparameter-axis and isolation plots
12. Search-boundary checks
13. Adoption decisions
14. End of exploration
15. Research interpretation rules

## 1. Incremental tuning strategy

The central workflow is iterative:

1. choose a scoped goal;
2. design and run a study;
3. extract as much information as possible;
4. decide whether the incumbent should change;
5. use the new understanding to design the next round.

The point is not merely to accumulate score improvements. The point is to progressively build a model of the tuning problem itself.

### Why not search everything at once?

The full configuration space is too large. Automated optimizers still depend on a human-designed search space, and poor search-space design can dominate algorithm choice.

Human guidance is therefore used to:

- decide what is scientifically interesting;
- fix irrelevant or understood dimensions;
- widen/narrow search spaces;
- spot confounds and failure modes;
- reject unnecessary complexity;
- decide when a new configuration is credible enough to become the baseline.

## 2. Exploration versus exploitation

### Exploration

Primary goal: gain insight.

Useful outputs of an exploratory round include:

- sensitivity ranking of hyperparameters;
- interaction structure;
- evidence that some variables can be fixed;
- evidence that a feature does not help;
- improved search ranges;
- diagnosis of overfitting or undertraining;
- identification of a bottleneck;
- discovery that tuning gains are saturating.

A study can be scientifically successful even if it does not produce a new best score, provided it reliably eliminates a hypothesis or clarifies the problem.

### Exploitation

Primary goal: select the strongest final configuration.

Use exploitation when the problem is mature enough that:

- the important variables are known;
- search ranges are reasonably localized;
- interaction risks are understood;
- the team needs a final launch/submission configuration.

## 3. Choosing one experimental goal

A round should have one dominant question.

Examples:

- Does regularizer X help?
- How sensitive is performance to context length?
- Does a deeper model improve best achievable validation performance?
- Is optimizer A better than optimizer B after fair tuning?
- Can we reduce latency without losing quality?

Avoid mixing unrelated scientific questions because the result becomes difficult to attribute.

### When multiple changes are acceptable

Sometimes the user explicitly wants an engineering bundle rather than a scientific attribution test. In that case:

- label the experiment as a **bundle comparison**;
- do not claim which component caused the gain;
- follow with ablations if component-level claims are needed.

## 4. Variable roles

The role of a hyperparameter is defined by the experimental question, not by the parameter itself.

### Scientific variable

The factor whose effect is being studied.

### Nuisance variable

A factor that must be adjusted so the scientific comparison is fair.

### Fixed variable

A factor held constant to make the study tractable.

### Role-switch example

Activation function can be:

- scientific: comparing ReLU vs GELU;
- nuisance: comparing depths while allowing each depth to select its best activation;
- fixed: studying another feature only in GELU models.

Always classify variables per study.

## 5. Conditional hyperparameters

A conditional variable only exists under some scientific setting.

Examples:

- Adam beta values only when optimizer=Adam;
- momentum only when optimizer=momentum SGD;
- memory-bank size only when memory module=enabled;
- auxiliary loss weight only when auxiliary loss=enabled.

### Key rule

Do not share numeric ranges across conditions without justification.

The learning-rate ranges for two optimizers may differ by orders of magnitude. Treat them as distinct search variables even if both are called `learning_rate`.

## 6. Building studies

A study specifies:

- scientific settings to compare;
- nuisance variables to tune;
- fixed variables;
- search spaces;
- number of trials;
- sampling/search procedure;
- run length;
- evaluation method;
- checkpoint-selection rule;
- repeat/seed policy.

### Separate-study pattern

For each scientific setting:

1. hold the scientific setting fixed;
2. tune nuisance variables;
3. select the best trial using the same rule;
4. compare the optimized results across scientific settings.

This is often cleaner when conditional nuisance variables differ across settings.

### Joint-study pattern

A single study may sample both scientific and nuisance variables together. Use only if:

- the sampling gives sufficient coverage per scientific setting;
- analysis can recover fair comparisons;
- conditional spaces are encoded correctly.

## 7. Allocating trial budget

Every finite study trades off:

### Scientific coverage

How many scientific settings are compared?

### Nuisance breadth

How many nuisance dimensions and how wide are their ranges?

### Nuisance density

How many samples land in each meaningful region?

A weak study often fails because it tries to maximize all three with too few trials.

### Budget design procedure

1. Identify the minimum scientific settings needed to answer the question.
2. Identify nuisance variables most likely to change the ranking.
3. Give those nuisance variables plausible wide ranges.
4. Estimate the number of trials available.
5. Reduce low-value dimensions if the space will be too sparse.
6. State what is fixed and what claim limitation follows.

## 8. Search-space design

### Range selection

Use:

- literature/defaults as initial anchors;
- prior studies on the same pipeline;
- pilot sweeps;
- physical/architectural constraints;
- failure regions discovered previously.

### Scale choice

Use a logarithmic or log-uniform interpretation for variables such as:

- learning rate;
- weight decay;
- epsilon-like scales;
- loss coefficients spanning orders of magnitude.

Use linear-like spacing when absolute differences are naturally meaningful.

### Boundary rule

If top trials accumulate at the minimum or maximum allowed value, the study did not establish an interior optimum.

Action:

- expand the boundary if plausible;
- rerun enough trials to see whether performance continues improving;
- avoid declaring the boundary value optimal simply because it won inside a truncated search.

### Infeasible trials

A search may include values that:

- diverge;
- exceed memory;
- violate model constraints;
- produce numerical errors.

Track these outcomes. They are evidence about the feasible region. After the region is understood, shrink obviously useless ranges to spend trials more efficiently.

## 9. Sampling/search algorithms

### Exploration phase

Simple quasi-random sampling is attractive because it:

- covers the space more uniformly than naive random sampling;
- is easy to parallelize;
- makes axis plots easier to interpret;
- does not depend strongly on launch order;
- behaves predictably when many trials run concurrently.

The playbook emphasizes that a better search space with more trials can matter more than a sophisticated optimizer.

### Exploitation phase

Adaptive methods such as Bayesian optimization become more useful when:

- the region of interest is already narrowed;
- trials can be launched sequentially enough to use feedback;
- the implementation handles invalid points and conditional variables well;
- expertise/tooling exists to avoid optimizer misuse.

## 10. Analyzing study results

Do not reduce a study to `max(score)`.

For every important study inspect:

- distribution of scores;
- top-k trials;
- hyperparameter values of top trials;
- search boundaries;
- training curves;
- validation curves;
- failures/infeasible trials;
- correlations/interactions among important hyperparameters;
- whether different scientific settings received comparable tuning quality.

### Study adequacy question

Ask:

> Was the nuisance space searched broadly and densely enough that the ranking between scientific settings is believable?

If no, the result is **HOLD**, not a strong scientific conclusion.

## 11. Hyperparameter-axis and isolation plots

### Axis plot

Plot a hyperparameter value against trial performance.

Use it to inspect:

- sensitivity;
- promising regions;
- flat regions;
- edge optima;
- nonlinear behavior;
- obvious interactions when conditioned on another variable.

Generate these plots automatically for all varied hyperparameters when feasible.

### Isolation-style plot

For each value of a scientific variable:

1. optimize over nuisance variables;
2. take the best or otherwise consistently selected nuisance-optimized result;
3. plot scientific value vs optimized performance.

This approximates the question:

> If I tune each scientific choice fairly, which choice is better?

### Important caveat

If one scientific value received more nuisance trials or a wider/better search space, its apparent advantage may be search-budget bias.

## 12. Search-boundary checks

For every tuned variable, ask:

- Is the best trial at a range edge?
- Are many good trials at the same edge?
- Do bad trials occupy the opposite edge?
- Is the range so broad that most trials are wasted?
- Is the range so narrow that uncertainty is hidden?

Boundary problems should be corrected before strong conclusions.

## 13. Adoption decisions

A new best validation score is not sufficient.

Before adopting:

1. check fairness of nuisance tuning;
2. inspect curves;
3. check search boundaries;
4. estimate run-to-run variance;
5. consider search/study variance;
6. confirm evaluation consistency;
7. assess complexity/resource cost.

### Decision categories

#### ADOPT

Use when the gain is credible and worthwhile.

#### REJECT

Use when the change fails to improve the relevant tradeoff or introduces unacceptable cost.

#### HOLD

Use when:

- search was underpowered;
- variance is comparable to the gain;
- candidate and baseline were not tuned fairly;
- evaluation differs;
- curves show unresolved failure;
- search boundaries are unresolved.

### Complexity tax

A change that adds parameters, code, latency, memory, tuning dimensions, or operational fragility should require more benefit than a zero-cost change.

## 14. End of exploration

Exploration is mature when:

- key variables have sensible search spaces;
- insensitive variables are fixed;
- harmful features are removed;
- major interactions are known;
- candidate configurations are stable enough to compare;
- the main remaining objective is obtaining the strongest final configuration.

Then:

- narrow ranges around good regions;
- spend more trials in those regions;
- consider adaptive black-box optimization;
- run final candidates with production/full training budgets;
- repeat important candidates to characterize variance.

## 15. Research interpretation rules

### Do not overclaim

If the experiment fixed architecture A, dataset B, and schedule C, a result may only establish the claim under those choices.

### Negative results are informative

A well-powered fair comparison that shows no benefit can simplify the pipeline and shrink future search spaces.

### Tuning is part of the method comparison

A method that only wins under one lucky hyperparameter point is different from a method that wins robustly across a reasonable tuning procedure.

### Prefer information gain

When choosing the next study, ask which experiment most reduces uncertainty relevant to the research decision, not which experiment is easiest to launch.
