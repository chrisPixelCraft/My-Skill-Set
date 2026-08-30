# Failure Diagnosis and Evidence Quality

## Contents

1. Diagnostic philosophy
2. Measurement failures
3. Data failures
4. Training-curve diagnosis
5. Overfitting
6. Undertraining / compute-bound behavior
7. Excessive step-to-step variance
8. Divergence and instability
9. Learning rate, warmup, gradient clipping
10. Search-space failures
11. Tuning-fairness failures
12. Trial, study, and data variance
13. Complexity failures
14. Debugging decision tree

## 1. Diagnostic philosophy

When a result is bad, surprising, or unstable, first search for explanations that invalidate the measurement or experiment before creating a new scientific story.

Priority:

1. Can the metric be trusted?
2. Can the data path be trusted?
3. Can the training implementation be trusted?
4. Was the configuration searched fairly?
5. Was the run long enough?
6. Is the candidate genuinely worse/better?
7. Only then ask whether the method hypothesis is wrong.

## 2. Measurement failures

### Symptoms

- validation score jumps periodically without corresponding training changes;
- restored checkpoint score differs from in-training evaluation;
- multi-host score differs from single-host score unexpectedly;
- metric changes when evaluation batch size changes;
- candidate looks better on proxy evaluation but worse on full evaluation.

### Checks

- verify metric implementation on hand-constructed cases;
- compare predictions across evaluation paths;
- check weighting of padded/partial batches;
- confirm no train/validation overlap;
- confirm all evaluation examples are counted once;
- compare sampled proxy against full evaluation;
- confirm deterministic preprocessing in evaluation mode where intended.

## 3. Data failures

### Potential problems

- leakage between splits;
- duplicated examples;
- incorrect labels;
- inconsistent preprocessing;
- train/eval normalization mismatch;
- improper shuffling;
- host sharding omission/duplication;
- stale cached data;
- augmentation enabled during evaluation accidentally.

### Evidence to collect

- dataset hashes/version IDs;
- split-generation code;
- per-class/sample counts;
- example visualizations;
- sample IDs from each split;
- preprocessing configs;
- host-level shard counts.

## 4. Training-curve diagnosis

Never inspect only the final scalar.

For top trials plot at least:

- training objective vs step;
- validation objective/metric vs step;
- learning rate vs step;
- gradient norm vs step when instability is plausible;
- throughput vs step if systems instability is plausible.

Optional useful plots:

- parameter/update norm;
- activation statistics;
- memory use;
- reward/success decomposition;
- per-task/per-class metrics;
- evaluation sample counts.

## 5. Overfitting

### Signature

Training improves while validation begins to degrade.

### Consequence for scientific comparison

If one scientific setting overfits because regularization was not tuned sufficiently, comparing its raw best/default configuration to another setting may be unfair.

### Actions

- tune existing regularization strength;
- introduce a scientifically justified regularizer;
- inspect augmentation;
- inspect model capacity;
- verify checkpoint selection;
- verify validation noise is not masquerading as overfitting.

Do not automatically add multiple regularizers. Introduce changes incrementally so the cause can be learned.

## 6. Undertraining / compute-bound behavior

### Signature

Best validation checkpoint occurs near the training budget boundary and curves continue improving.

### Actions

- increase run length for a small subset;
- reconsider learning-rate schedule length;
- use staged short-to-long experiments;
- verify that candidate/baseline have equal opportunity to benefit from longer training.

### Scientific warning

A method that learns more slowly may look worse under a short fixed budget but better asymptotically. Decide whether the research claim concerns fixed compute or best achievable performance.

## 7. Excessive step-to-step variance

### Potential sources

- small stochastic batches;
- small/noisy validation sample;
- learning rate too high late in training;
- aggressive stochastic augmentation;
- environment stochasticity in RL/robotics;
- nondeterministic distributed execution.

### Possible interventions

- larger batch where appropriate;
- larger evaluation sample;
- learning-rate decay;
- averaging/smoothing methods when scientifically appropriate;
- more evaluation episodes;
- multiple seeds.

Do not smooth away instability and then claim the underlying process is stable. Preserve raw curves.

## 8. Divergence and instability

### Symptoms

- loss becomes NaN/Inf;
- sudden large loss spikes;
- gradient norm spikes;
- weights/activations explode;
- instability appears early after startup;
- instability appears mid-training after apparently healthy progress.

### Investigation order

1. reproduce the failure;
2. inspect learning rate and schedule;
3. log unclipped gradient norms;
4. check numerical precision/loss scaling;
5. inspect data batches near failure if possible;
6. inspect distributed synchronization;
7. test warmup;
8. test gradient clipping;
9. reduce learning rate if clipping must be extreme.

## 9. Learning rate, warmup, gradient clipping

### Warmup

Warmup can prevent early-training instability at learning rates that are otherwise useful later.

When adding warmup:

- ensure the total training budget still gives the model sufficient time after warmup;
- do not accidentally compare a baseline with N effective training steps to a candidate with substantially fewer effective steps;
- treat warmup length as a relevant nuisance variable if it materially changes the comparison.

### Gradient clipping

Gradient clipping is most justified when gradient outliers cause instability.

Good practice:

- log **unclipped** gradient norms;
- inspect their distribution;
- choose a threshold relative to typical norms;
- verify what fraction of steps are clipped.

If most updates require strong clipping, clipping may be acting as an indirect learning-rate reduction. Reconsider the learning rate rather than relying on extreme clipping.

## 10. Search-space failures

### Too narrow

Symptoms:

- best trials at edges;
- all configurations similar;
- known-good defaults outside range.

Fix: widen range.

### Too wide

Symptoms:

- most trials diverge or are obviously poor;
- very few samples in the plausible good region.

Fix: use exploration results to narrow ranges.

### Too many nuisance variables

Symptoms:

- space is high-dimensional;
- each scientific condition receives only a handful of useful trials;
- ranking changes between search seeds.

Fix: fix low-sensitivity variables or increase budget.

### Wrong scale

Symptom: values are sampled densely in an irrelevant numeric region.

Fix: use a scale that matches parameter semantics, often log scale for multiplicative quantities.

## 11. Tuning-fairness failures

### Default-vs-tuned bias

One method uses published defaults while another receives extensive optimization.

Correction: define equal or scientifically defensible tuning budgets.

### Shared hyperparameter bias

The same numeric learning rate is forced across architectures/optimizers.

Correction: treat learning rate as nuisance and retune per scientific setting when interaction is plausible.

### Unequal training opportunity

One method converges slower but all methods are compared at an arbitrary short step count.

Correction: specify whether the claim is fixed-budget performance or best-achievable performance and design accordingly.

### Unequal checkpoint selection

Candidate uses best checkpoint while baseline uses last checkpoint.

Correction: use the same retrospective selection procedure.

## 12. Trial, study, and data variance

### Trial/retrain variance

Same hyperparameters, different stochastic run.

Estimate with repeated seeds when the decision warrants the cost.

### Study/search variance

Different hyperparameter samples can produce different selected winners.

This matters especially when comparing the best results from underpowered searches.

Possible check:

- rerun the search with another quasi-random seed;
- compare top configurations;
- inspect whether the scientific ranking is stable.

### Data/sampling variance

Different split or evaluation sample can alter the result.

Check when:

- dataset is small;
- classes/tasks are highly imbalanced;
- success metrics use few episodes;
- the claimed gain is small.

### Decision principle

Do not insist on absolute certainty. Instead estimate whether the observed gain is materially larger than the uncertainty relevant to the deployment/research decision.

## 13. Complexity failures

A technically positive result can still be a bad adoption.

Reject or hold when the gain is too small relative to:

- new failure modes;
- extra model branches;
- extra hyperparameters;
- training-time cost;
- inference latency;
- memory;
- preprocessing dependency;
- deployment difficulty;
- reproducibility burden.

Complexity also makes future science harder because every new component can interact with later experiments.

## 14. Debugging decision tree

Use the first matching branch.

### A. Result is implausibly good

Check:

1. leakage;
2. duplicate validation/test examples;
3. metric bug;
4. wrong split;
5. accidental use of labels/future information;
6. checkpoint/evaluation mismatch.

### B. Result is implausibly bad

Check:

1. data preprocessing;
2. label mapping;
3. learning-rate range;
4. optimizer config;
5. run length;
6. checkpoint restore;
7. evaluation mode;
8. baseline reproduction.

### C. Candidate wins once, loses on repeat

Check:

1. trial variance;
2. search variance;
3. data sampling variance;
4. whether winner was at search boundary;
5. whether candidate received more tuning budget.

### D. Training diverges early

Check:

1. learning rate;
2. warmup;
3. gradient norm;
4. precision/loss scaling;
5. initialization;
6. invalid data.

### E. Training diverges mid-run

Check:

1. gradient spikes;
2. schedule transitions;
3. rare bad batches;
4. optimizer state;
5. distributed synchronization;
6. numerical overflow.

### F. Training is slow

Check:

1. accelerator utilization;
2. profiler trace;
3. input I/O;
4. preprocessing;
5. prefetching;
6. synchronization;
7. communication overhead.

### G. Validation peaks early

Check:

1. overfitting;
2. regularization;
3. learning-rate schedule;
4. step budget;
5. checkpoint selection.

### H. Validation still rises at end

Check:

1. longer budget;
2. schedule extension;
3. short-vs-long ranking transfer;
4. whether compute budget defines the actual research claim.
