# Training Budget, Evaluation, Checkpointing, and Pipeline Reliability

## Contents

1. Choosing training length
2. Not-compute-bound regime
3. Compute-bound regime
4. Learning-rate interaction
5. Input-pipeline performance
6. Evaluation settings
7. Periodic evaluation
8. Evaluation sampling
9. Checkpoint selection
10. Experiment tracking
11. BatchNorm caveats
12. Multi-host caveats
13. Pipeline review checklist

## 1. Choosing training length

Training length is an experimental design choice, not merely an implementation detail.

A run that is too short can make a good method look bad. A run that is excessively long slows iteration and consumes budget that could have answered more questions.

The correct strategy depends on whether performance is limited by the training budget.

## 2. Not-compute-bound regime

Symptoms:

- training and validation performance saturate well before the final step;
- retrospective best checkpoints repeatedly occur early;
- additional steps rarely improve best achievable validation performance.

### Procedure

1. Pick a common `max_train_steps` for all trials in the study.
2. Save checkpoints throughout training.
3. Select the best checkpoint retrospectively using the same validation rule.
4. Plot the selected-best step for top trials.
5. If best steps cluster very early, lower the budget in a future round.
6. If best steps cluster near the end, consider increasing the budget.

### Hard rule

Do not tune `max_train_steps` as another hyperparameter inside an ordinary study. Doing so can give different trials unequal opportunities and complicate interpretation.

### Why longer can be safe in this regime

If checkpoint selection is retrospective and sufficiently frequent, running longer should not force use of a worse late checkpoint. The main cost is compute/time.

## 3. Compute-bound regime

Symptoms:

- training or validation performance is still improving near the end;
- the best checkpoint repeatedly occurs at the final portion of training;
- substantially longer runs could plausibly help, but compute or deadlines prevent exhaustive tuning.

### Research strategy

Do not run every exploratory idea at maximum production length.

Instead:

1. create a shorter exploration budget;
2. tune many ideas at that budget;
3. identify robust candidates;
4. promote only strong candidates to longer runs;
5. verify that rankings and hyperparameter choices remain valid at longer duration.

This is a staged de-risking pipeline.

### Transfer risk

A hyperparameter setting optimal for short runs may not be optimal for long runs. Learning-rate schedule and regularization interactions are especially important.

Therefore promotion to longer training should be treated as a new evidence stage, not as a mechanical extrapolation.

## 4. Learning-rate interaction

Training length and learning-rate schedule are coupled.

If the run length changes:

- schedule decay timing may need to change;
- warmup fraction may need reconsideration;
- base learning rate may transfer or may need retuning;
- longer high-learning-rate phases may be useful in some regimes.

Avoid interpreting a long-vs-short training comparison when the schedule makes one condition artificially disadvantaged.

## 5. Input-pipeline performance

An accelerator waiting for data creates slower experiments without improving science.

### Diagnose with profiling

Use a profiler appropriate to the framework/hardware.

Potential symptoms:

- low accelerator utilization;
- periodic stalls;
- input time comparable to compute time;
- strong speed sensitivity to storage/network location.

### Common causes

- data stored far from compute;
- network I/O latency;
- expensive preprocessing executed online every epoch;
- host/device synchronization barriers;
- missing or shallow prefetching;
- carrying unused metadata/features;
- too few parallel data workers.

### Interventions

- colocate or cache data;
- precompute expensive deterministic preprocessing;
- increase prefetching;
- remove unused fields early;
- increase data-worker/service parallelism;
- remove accidental synchronization points.

### Scientific caveat

Do not change preprocessing semantics merely to improve throughput unless the scientific effect is understood. A faster pipeline that changes the data distribution is a different experiment.

## 6. Evaluation settings

Evaluation can be:

### Online

Measured in the actual deployed environment. Often the most realistic, but expensive or unavailable during research.

### Offline

Measured on train/validation/test datasets intended to represent deployment.

### Periodic

Measured during training on a convenient full or sampled evaluation set.

The periodic metric is often a proxy used for:

- monitoring;
- checkpoint selection;
- training-curve analysis;
- rapid experiment comparison.

Validate that this proxy tracks the more authoritative offline/online evaluation well enough for the intended decision.

## 7. Periodic evaluation

### Step-based cadence

Evaluate at regular training-step intervals rather than regular wall-clock intervals.

This makes curves more interpretable when jobs experience:

- preemption;
- network stalls;
- variable input speed;
- host contention.

### Evaluation batch size

When memory allows, use a batch size at least as large as training. Evaluation does not need to retain gradient-related state.

### Bug signal

Unexpected periodic patterns in validation/test metrics can indicate:

- data overlap;
- improper shuffling;
- repeated evaluation subsets;
- state leakage;
- synchronization bugs.

## 8. Evaluation sampling

When full evaluation is too expensive, choose a sample that is:

- small enough to evaluate frequently;
- large enough to distinguish meaningful improvements from noise;
- representative of the full evaluation distribution.

### Required validation

Compare sampled-evaluation metrics with full offline evaluation for a selection of checkpoints/models.

If the sampled set is biased, it can optimize the wrong model.

### Imbalanced data

Rare classes produce noisy aggregate metrics.

Record raw counts where useful. A large percentage change may correspond to one additional correct example.

### Adaptive overfitting risk

Repeatedly selecting research decisions using the same validation set can gradually overfit the research process to that set. Preserve a held-out test set for final claims when feasible.

## 9. Checkpoint selection

### Retrospective selection

Save checkpoints during a fixed-length run and choose the best checkpoint after training.

Advantages:

- the final step need not be optimal;
- temporary validation degradation does not force a bad final model;
- comparisons can use the same run budget;
- step location of best checkpoints becomes diagnostic evidence.

### Frequency

Checkpoint/evaluation intervals must be frequent enough not to miss meaningful peaks.

### Comparability

All compared methods should use the same selection policy unless the difference is itself part of the method.

## 10. Experiment tracking

A study should be reconstructable without relying on memory.

Track at minimum:

- study identifier;
- experiment question;
- configuration path or serialized config;
- repository revision/commit;
- uncommitted diff note if relevant;
- launch command;
- dataset version/split;
- number of trials;
- random seeds;
- hardware/resource notes;
- training duration;
- best validation metric;
- checkpoint identifier/path;
- key plots;
- known failures;
- decision: adopt/reject/hold;
- reason for decision.

The playbook's message is uncompromising: an experiment that cannot be tracked and reconstructed has little durable research value.

## 11. BatchNorm caveats

Batch normalization can make apparently simple batch-size or multi-device comparisons scientifically confounded.

Audit:

- which examples contribute to statistics;
- per-device vs synchronized statistics;
- virtual/ghost batch behavior;
- moving-average synchronization;
- checkpoint behavior;
- inference-time statistics.

If batch size changes the BatchNorm statistic regime, the experiment changed more than batch size alone.

## 12. Multi-host caveats

Multi-host training increases the surface area for silent bugs.

### Logging/checkpointing

Use one designated writer unless the framework safely coordinates multiple writers.

### RNG

Separate the concepts:

- model initialization may need identical state across hosts;
- data shuffling and stochastic preprocessing often need different host-specific randomness.

### Statistics

Synchronize global statistics before evaluation or checkpointing when required.

### Data

Shard data deliberately. Confirm examples are neither unintentionally duplicated nor omitted.

### Evaluation

Confirm multi-host evaluation aggregates examples and metrics exactly once.

## 13. Pipeline review checklist

- [ ] Is accelerator utilization healthy?
- [ ] Is data loading profiled rather than guessed?
- [ ] Are preprocessing semantics unchanged by performance optimizations?
- [ ] Is evaluation step-based?
- [ ] Does periodic evaluation correlate with authoritative evaluation?
- [ ] Is sampled evaluation representative?
- [ ] Are padded/partial batches weighted correctly?
- [ ] Are predictions/examples preserved for debugging when practical?
- [ ] Are checkpoints frequent enough?
- [ ] Is the same checkpoint-selection rule used across conditions?
- [ ] Is `max_train_steps` fixed within a study?
- [ ] Are best-checkpoint positions inspected?
- [ ] Is experiment metadata sufficient to reproduce a run?
- [ ] If BatchNorm is used, are statistics comparable?
- [ ] If multi-host is used, are RNG, logging, statistics, data sharding, and evaluation semantics audited?
