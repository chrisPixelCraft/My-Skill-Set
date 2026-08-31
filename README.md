# My Skill Set

Reusable agent skills for careful reasoning, readable documentation, and
evidence-driven AI/ML research. Each skill is self-contained: Codex first uses
its name and description for routing, then loads the full `SKILL.md` only when
the task matches.

## Included skills

| Skill | Use it for |
|---|---|
| [`human-readable-docs`](Skillset/human-readable-docs/SKILL.md) | Writing and revising human-facing Markdown, READMEs, research notes, experiment reports, benchmark summaries, and design docs without losing technical evidence. |
| [`paper-figure-experiment-design`](Skillset/paper-figure-experiment-design/SKILL.md) | Auditing or designing AI/ML paper methods, teaser and motivation figures, method diagrams, and claim-testing experiment matrices. |
| [`paper-story-design`](Skillset/paper-story-design/SKILL.md) | Designing or auditing a paper's claim-driven visual narrative, including teaser figures, method diagrams, and identifiable experiment suites. |
| [`ponder-research`](Skillset/ponder-research/SKILL.md) | Scientific reasoning that involves hypotheses, mechanisms, experiment design, literature synthesis, causal interpretation, research taste, or belief updates. |
| [`thinking-protocol`](Skillset/thinking-protocol/SKILL.md) | Careful, adaptive, multi-perspective reasoning for complex engineering, debugging, architecture, research, and document-analysis tasks. |
| [`tuning-playbook-research`](Skillset/tuning-playbook-research/SKILL.md) | Planning, reviewing, diagnosing, and interpreting ML/DL experiments with fair tuning, explicit variable roles, variance checks, and evidence-based adoption decisions. |

These skills are intentionally scoped. They should activate only when their
descriptions match the task, rather than adding a mandatory workflow to every
request.

## Install

Codex supports personal skills in `~/.agents/skills` and repository-scoped
skills in `<repo>/.agents/skills`. It also follows symlinked skill directories.
See the [official OpenAI skill documentation](https://developers.openai.com/codex/skills)
for the current loading rules and supported locations.

### Use the skill installer

Paste this request into Codex and remove any skills you do not want:

```text
Use $skill-installer to install these skills:
- https://github.com/chrisPixelCraft/My-Skill-Set/tree/main/Skillset/human-readable-docs
- https://github.com/chrisPixelCraft/My-Skill-Set/tree/main/Skillset/paper-figure-experiment-design
- https://github.com/chrisPixelCraft/My-Skill-Set/tree/main/Skillset/paper-story-design
- https://github.com/chrisPixelCraft/My-Skill-Set/tree/main/Skillset/ponder-research
- https://github.com/chrisPixelCraft/My-Skill-Set/tree/main/Skillset/thinking-protocol
- https://github.com/chrisPixelCraft/My-Skill-Set/tree/main/Skillset/tuning-playbook-research
```

### Install all skills manually

Clone the repository, then symlink every valid skill into your personal skill
directory:

```bash
git clone https://github.com/chrisPixelCraft/My-Skill-Set.git
cd My-Skill-Set
mkdir -p ~/.agents/skills

for skill_dir in "$PWD"/Skillset/*; do
  [ -f "$skill_dir/SKILL.md" ] || continue
  skill_name="$(basename "$skill_dir")"
  skill_destination="$HOME/.agents/skills/$skill_name"

  if [ -e "$skill_destination" ] || [ -L "$skill_destination" ]; then
    printf 'Skipping existing skill: %s\n' "$skill_name"
    continue
  fi

  ln -s "$skill_dir" "$skill_destination"
done
```

The loop skips existing destinations instead of overwriting or nesting inside
an existing installation. Resolve skipped skills explicitly.

For project-only use, copy or symlink selected skill folders into the target
repository's `.agents/skills/` directory.

## Use

Codex can invoke a skill implicitly when a request matches its description. To
select one explicitly, mention it with `$skill-name` in the prompt:

```text
$human-readable-docs rewrite this benchmark report for a technical reader.

$paper-figure-experiment-design design a teaser, method figure, and claim-testing experiment matrix.

$paper-story-design audit this paper's visual narrative and evidence coverage.

$ponder-research challenge this hypothesis and design the cheapest decisive experiment.

$thinking-protocol review this architecture and verify the important assumptions.

$tuning-playbook-research diagnose these training curves and recommend the next study.
```

In Codex CLI or the IDE extension, `/skills` shows available skills. If a newly
installed or changed skill does not appear, restart Codex.

## Repository layout

```text
Skillset/
├── human-readable-docs/
│   └── SKILL.md
├── paper-figure-experiment-design/
│   ├── SKILL.md
│   ├── agents/
│   │   └── openai.yaml
│   ├── references/
│   │   ├── 5w2h-templates.md
│   │   ├── corpus-evidence.md
│   │   ├── experiment-design.md
│   │   ├── method-design.md
│   │   └── visual-grammar.md
│   └── scripts/
│       └── inventory_paper_figures.py
├── paper-story-design/
│   ├── SKILL.md
│   ├── agents/
│   │   └── openai.yaml
│   └── references/
│       ├── evidence-base.md
│       ├── experiment-story.md
│       ├── questions-and-templates.md
│       ├── verifier-gates.md
│       └── visual-story.md
├── ponder-research/
│   └── SKILL.md
├── thinking-protocol/
│   └── SKILL.md
└── tuning-playbook-research/
    ├── SKILL.md
    ├── agents/
    │   └── openai.yaml
    └── references/
        ├── failure_diagnosis.md
        ├── project_start.md
        ├── scientific_tuning.md
        ├── source_map.md
        ├── templates.md
        └── training_pipeline.md
```

A minimal skill is a directory containing a `SKILL.md` with `name` and
`description` frontmatter. Larger skills may add focused references, scripts,
assets, or `agents/openai.yaml` metadata.

## Attribution

`tuning-playbook-research` is an independent, paraphrased procedural adaptation
of Google Research's
[Deep Learning Tuning Playbook](https://github.com/google-research/tuning_playbook).
It is not an official Google product. The detailed mapping and scope limitations
are documented in its
[`source_map.md`](Skillset/tuning-playbook-research/references/source_map.md).
