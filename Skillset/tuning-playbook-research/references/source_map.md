# Source Map and Scope

## Primary source

**Deep Learning Tuning Playbook**

Authors: Varun Godbole, George E. Dahl, Justin Gilmer, Christopher J. Shallue, Zachary Nado

Repository: https://github.com/google-research/tuning_playbook

Cited version in the repository: Version 1.0 (2023)

The repository states that the playbook is not an officially supported Google product and presents the authors' practical views rather than objective universal truth.

## Skill construction note

This skill is a detailed **paraphrased procedural adaptation**. It preserves the playbook's concepts, decision structure, terminology, and practical recommendations while avoiding long verbatim reproduction.

One short line from the source captures the tracking principle:

> "Untracked experiments might as well not exist."

## Original sections represented

### Audience and motivation

Mapped into:

- `SKILL.md` Purpose / Non-goals
- evidence-first operating philosophy

### Guide for starting a new project

Original topics:

- choosing architecture;
- choosing optimizer;
- choosing batch size;
- choosing initial configuration.

Mapped into:

- `references/project_start.md`
- `SKILL.md` Special rules

### Scientific approach to improving model performance

Original topics:

- incremental tuning;
- exploration vs exploitation;
- choosing the goal for the next round;
- scientific/nuisance/fixed hyperparameters;
- conditional hyperparameters;
- creating studies;
- choosing search spaces;
- examining results and curves;
- isolation plots;
- deciding whether to adopt changes;
- transition from exploration to final optimization.

Mapped into:

- `references/scientific_tuning.md`
- `SKILL.md` Core protocol

### Determining the number of training steps

Original topics:

- non-compute-bound training;
- compute-bound training;
- fixed step budgets within a study;
- using best-checkpoint locations to refine training length;
- staged short-to-long tuning.

Mapped into:

- `references/training_pipeline.md`

### Additional training-pipeline guidance

Original topics:

- input pipeline profiling;
- periodic evaluation;
- evaluation sampling;
- checkpointing and retrospective selection;
- experiment tracking;
- BatchNorm details;
- multi-host issues.

Mapped into:

- `references/training_pipeline.md`
- `references/failure_diagnosis.md`

### FAQ / practical tuning topics

The source also discusses topics such as:

- learning-rate schedules;
- quasi-random search;
- warmup;
- gradient clipping;
- optimizer parameter details.

Mapped selectively into:

- `SKILL.md` Search algorithm / Training duration
- `references/failure_diagnosis.md`

## Scope limitations of the original playbook

The playbook mainly assumes a supervised-learning problem or something structurally similar and assumes that problem formulation, data cleaning, metric selection, and a functioning training/evaluation pipeline already exist.

When applying this skill to RL, robotics, generative modeling, or online systems, translate the experimental roles rather than copying supervised-learning mechanics literally.

Examples:

- validation examples -> evaluation episodes/tasks;
- trial variance -> seed/environment/rollout variance;
- training step -> optimizer/update/environment step as appropriate;
- validation metric -> success rate/reward/task metric;
- data sampling variance -> environment/task/episode sampling variance.

The scientific principles still apply: fair nuisance tuning, fixed-choice caveats, careful evaluation, curve inspection, variance characterization, and evidence-based adoption.
