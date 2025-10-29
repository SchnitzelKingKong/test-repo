#!/usr/bin/env bash
set -euo pipefail

FORCE=0
while [[ ${1-} ]]; do
  case "$1" in
    --force) FORCE=1 ; shift ;;
    *) echo "Unknown arg: $1" >&2; exit 1 ;;
  esac
done

mkdir -p .codex
mkdir -p .codex/templates

# Resolve global templates (optional)
GLOBAL_TEMPLATES_DIR="${HOME:-$PWD}/.codex/templates"

create_if_absent() {
  local path="$1"; shift
  if [[ -f "$path" && $FORCE -eq 0 ]]; then
    echo "skip: $path exists (use --force to overwrite)"
    return 0
  fi
  cat > "$path" <<'EOF'
__CONTENT__
EOF
  # Remove placeholder line
  sed -i '1{/^__CONTENT__$/d;}' "$path"
  echo "write: $path"
}

# NOTES.md default
cat > .codex/.NOTES.default <<'MD'
Project Summary
- One-liner: Exercises and notes for an ML course (TensorFlow, Kaggle, DS).
- Scope: Weekly notebooks, small scripts, and learning artifacts under `KW43/`.

Current Objective
- Build and train a simple Keras regression model (housing prices).

Key Decisions / Constraints
- Language: English primary, German fallback.
- Libraries: TensorFlow/Keras; experiments in `_misc/`.
- Data: Notebooks in `KW43/tensorflow/` and `kaggle_python/`.
- Environment: Workspace-write; network may be restricted in CLI.

Status
- Done: Notebook scaffolded; `model.compile(optimizer='adam', loss='mse', metrics=['mae'])` present.
- Blocked: Confirm dataset loading and preprocessing.

Open Tasks
- [ ] Verify dataset path and splits; avoid leakage.
- [ ] Fit model and plot learning curves.
- [ ] Tune LR and batch size; record outcomes.

Pointers
- Files: `KW43/tensorflow/Week1_Notebook1_Housing_Prices.ipynb`
- Files: `KW43/_misc/agent.py`
- Notes: `KW43/tensorflow/preperation-kw43.md`

Decisions Log
- <date> — Initialized .codex context scaffolding.

Next Steps
- Load data, normalize features, fit model; log metrics.
MD

# profile.yaml default
cat > .codex/.profile.default <<'YML'
preferences:
  language_primary: English
  language_fallback: German
  tone: concise-friendly
  code_style: minimal-diff, consistent-with-repo
  summarize_strategy:
    - keep NOTES.md up to date each session
    - pin key decisions and file references
    - trim long logs; store commands and outcomes
  context_usage:
    - reference file paths + line numbers
    - avoid pasting large blobs; link to files
    - break tasks into small steps

workspace:
  important_paths:
    - KW43/_misc/agent.py
    - KW43/tensorflow/Week1_Notebook1_Housing_Prices.ipynb
    - README.md
    - KW43/tensorflow/preperation-kw43.md

session:
  notes_file: .codex/NOTES.md
  instructions_file: .codex/instructions.md
YML

# instructions.md default
cat > .codex/.instructions.default <<'MD'
Using .codex for Context

- Maintain session context in `.codex/NOTES.md` (goals, decisions, status, open tasks, pointers).
- Capture preferences in `.codex/profile.yaml` (language, tone, workflow patterns).
- At the start of any new chat, reference these files by path so the agent can instantly regain context.

Suggested Workflow
- After meaningful changes, update NOTES.md sections.
- Log important decisions with date and rationale.
- Point to exact files and lines instead of pasting large chunks.

Quick Bootstrap Template
Context bootstrap
- Project: <one-liner>
- Current objective: <short>
- Key decisions: see .codex/NOTES.md (Decisions Log)
- Pointers: see .codex/NOTES.md (Pointers)
- Constraints: <env, versions, sandbox>
- Next steps: <1–3 items>
MD

# Write files (idempotent) using templates if present
SRC_NOTES=".codex/templates/NOTES.md"
if [[ ! -f "$SRC_NOTES" && -f "$GLOBAL_TEMPLATES_DIR/NOTES.md" ]]; then
  SRC_NOTES="$GLOBAL_TEMPLATES_DIR/NOTES.md"
fi
[[ -f "$SRC_NOTES" ]] || SRC_NOTES=".codex/.NOTES.default"

if [[ ! -f .codex/NOTES.md || $FORCE -eq 1 ]]; then
  cp "$SRC_NOTES" .codex/NOTES.md
  echo "write: .codex/NOTES.md"
else
  echo "skip: .codex/NOTES.md exists (use --force to overwrite)"
fi

SRC_PROFILE=".codex/templates/profile.yaml"
if [[ ! -f "$SRC_PROFILE" && -f "$GLOBAL_TEMPLATES_DIR/profile.yaml" ]]; then
  SRC_PROFILE="$GLOBAL_TEMPLATES_DIR/profile.yaml"
fi
[[ -f "$SRC_PROFILE" ]] || SRC_PROFILE=".codex/.profile.default"

if [[ ! -f .codex/profile.yaml || $FORCE -eq 1 ]]; then
  cp "$SRC_PROFILE" .codex/profile.yaml
  echo "write: .codex/profile.yaml"
else
  echo "skip: .codex/profile.yaml exists (use --force to overwrite)"
fi

SRC_INSTRUCTIONS=".codex/templates/instructions.md"
if [[ ! -f "$SRC_INSTRUCTIONS" && -f "$GLOBAL_TEMPLATES_DIR/instructions.md" ]]; then
  SRC_INSTRUCTIONS="$GLOBAL_TEMPLATES_DIR/instructions.md"
fi
[[ -f "$SRC_INSTRUCTIONS" ]] || SRC_INSTRUCTIONS=".codex/.instructions.default"

if [[ ! -f .codex/instructions.md || $FORCE -eq 1 ]]; then
  cp "$SRC_INSTRUCTIONS" .codex/instructions.md
  echo "write: .codex/instructions.md"
else
  echo "skip: .codex/instructions.md exists (use --force to overwrite)"
fi

echo "Done."
