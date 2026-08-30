# Project Start and Initial Configuration

## Contents

1. Preconditions
2. Architecture choice
3. Optimizer choice
4. Batch-size choice
5. Initial configuration
6. Initial run checklist
7. Common mistakes

## 1. Preconditions

The tuning workflow assumes foundational work is already good enough that model/training decisions are meaningful.

Before optimizing model performance, confirm:

- the problem is well formulated;
- data have been cleaned enough to support training;
- the train/validation/test split matches the intended claim;
- metrics are implemented correctly and represent the target environment as closely as practical;
- training and prediction jobs can be launched repeatedly;
- a basic training/evaluation pipeline exists.

If these are not true, spend the next iteration on stabilization rather than tuning.

## 2. Architecture choice

### Default stance

Start with a model family that is established and commonly used for the same or a closely related workload.

Why:

- known architectures reduce implementation uncertainty;
- published or community baselines provide approximate expectations;
- common architectures make it easier to distinguish a pipeline bug from an architecture problem;
- later custom architecture work becomes easier to attribute because the starting point is known.

Choosing an architecture usually means choosing a **family**, not a single model. Depth, width, activation, normalization, token count, context length, and similar choices create additional model hyperparameters.

### Research exception

If the architecture itself is the scientific question, the baseline should still be a credible established model. The new architecture becomes the scientific variable and its nuisance parameters must be tuned fairly.

## 3. Optimizer choice

### Default stance

Use a popular optimizer for the workload rather than spending the first research cycle searching for an exotic optimizer.

Reasons:

- no optimizer dominates all tasks;
- complex optimizers can add many nuisance hyperparameters;
- optimizer comparison itself is difficult because each optimizer may require different tuning effort and ranges.

### Practical rule

Early in a project, consider fixing secondary optimizer parameters to standard values and tuning the dominant ones, if that simplification is defensible.

Later, if optimizer performance is central, expand the optimizer-specific search.

### Fair optimizer comparison

If comparing optimizer families:

- optimizer family = scientific variable;
- learning rate = optimizer-conditional nuisance variable;
- momentum/betas/epsilon/etc. = optimizer-conditional nuisance or fixed variables;
- use ranges appropriate to each optimizer;
- do not force identical numeric ranges simply because parameters share a name.

## 4. Batch-size choice

### What batch size is for

Treat batch size primarily as a systems and training-speed decision.

Evaluate:

- accelerator memory limit;
- examples/second or tokens/second;
- step time;
- time to target performance;
- number of devices required;
- total GPU/TPU-hours;
- engineering cost of distributed training.

### Feasible-range discovery

When the maximum feasible batch size is unknown:

1. run short jobs at increasing batch sizes;
2. record whether compilation/training fits in memory;
3. measure steady-state throughput after warmup/startup effects;
4. compare wall-clock training efficiency rather than raw batch size.

### Important comparison distinction

A fixed **step budget** and a fixed **example/epoch budget** answer different questions.

When batch size changes, document which budget is held constant. Otherwise the comparison can silently mix optimization and compute effects.

### Operational heuristic

A large feasible batch is often useful when it reduces development latency, but do not add distributed complexity merely to maximize batch size. Multi-host code can create new correctness risks.

## 5. Initial configuration

The first configuration should optimize for **learning speed of the research process**, not for final leaderboard performance.

Prefer a configuration that is:

- simple;
- fast;
- relatively inexpensive;
- clearly better than trivial/random performance;
- easy to reproduce;
- easy to modify one factor at a time.

Examples of simplification:

- smaller model before a large model;
- simple learning-rate behavior before elaborate schedules;
- minimal regularization before stacking many regularizers;
- few preprocessing tricks before a large augmentation pipeline.

### Why simplicity matters

If a feature is present from the beginning, later researchers may never discover whether it was necessary. Each extra component adds tuning dimensions and interactions.

## 6. Initial run checklist

Before calling the baseline ready:

- [ ] training loss moves in the expected direction;
- [ ] validation performance is meaningfully above trivial chance/baseline;
- [ ] train/validation curves are logged;
- [ ] exact configuration is saved;
- [ ] code revision is saved;
- [ ] seed is recorded;
- [ ] runtime and resource use are recorded;
- [ ] checkpoints can be restored;
- [ ] evaluation results reproduce after restore;
- [ ] a second run does not reveal catastrophic run-to-run instability;
- [ ] failure cases can be inspected at least manually.

## 7. Common mistakes

### Starting from an overcomplicated baseline

Symptom: nobody knows which trick is responsible for performance.

Correction: remove optional components or treat them as later scientific variables.

### Optimizer shopping too early

Symptom: dozens of optimizer variants are explored before the data/evaluation pipeline is trusted.

Correction: pick a standard optimizer and stabilize the experiment system first.

### Batch size used as a validation-score knob

Symptom: batch size is tuned to maximize validation score without retuning learning rate/regularization or accounting for training budget.

Correction: treat batch size as throughput/resource choice and retune dependent hyperparameters when necessary.

### Starting too large

Symptom: each run takes days, so only a few ideas can be tested.

Correction: create a cheaper exploration configuration and later verify that conclusions transfer to full-scale training.
