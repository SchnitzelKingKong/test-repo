Agent Setup Instructions

Scope: Entire repository.

Purpose
- Ensure agents automatically restore project context at session start.

Required Startup Behavior
- On initialization, read and use these files (if present):
  - `.codex/NOTES.md` — authoritative, living context (goals, status, decisions, tasks, pointers).
  - `.codex/profile.yaml` — preferences (language, tone, code style, key paths).
  - `.codex/instructions.md` — workflow guidance; optional.

Guidelines for Agents
- Treat `.codex/NOTES.md` as the primary source of truth for current objectives and decisions.
- Prefer path + line references over large inline pastes.
- Keep diffs minimal and consistent with existing style.
- When updating context, append to NOTES.md (Status, Open Tasks, Decisions Log) instead of rewriting unrelated sections.

When Absent
- If `.codex/*` is missing, continue normally, but offer to scaffold it.

User Preferences (from profile.yaml)
- language_primary: English; language_fallback: German
- tone: concise-friendly
- code_style: minimal-diff, consistent-with-repo

Scaffolding (If Missing)
- If `.codex/` is absent, agents SHOULD propose creating it and, upon approval, generate files with sensible defaults:
  - `.codex/NOTES.md` seeded with: project summary, current objective, key decisions/constraints, status, open tasks, pointers, decisions log, next steps.
  - `.codex/profile.yaml` seeded with defaults:
    - `language_primary: English`, `language_fallback: German`
    - `tone: concise-friendly`
    - `code_style: minimal-diff, consistent-with-repo`
    - `workspace.important_paths`: discovered key files under `KW43/` and `README.md`
  - `.codex/instructions.md` describing how to use these files and a bootstrap template.
- Agents MAY run `scripts/setup_codex_context.sh` to scaffold these files (see below) after obtaining user confirmation when needed.

Bootstrap Entry Point (Single File)
- Preferred: `python scripts/agent_bootstrap.py` — performs detection + scaffolding using repo/global templates, then emits resolved paths to `.codex/NOTES.md` and `.codex/profile.yaml`.

Helper Script (Shell)
- Alternative: `bash scripts/setup_codex_context.sh` to create `.codex/` with defaults if missing or to refresh placeholders. Idempotent; pass `--force` to overwrite.

Global Templates
- The setup script also looks for user-wide templates in `~/.codex/templates/` and prefers them when repo templates are absent. Provide these files once to standardize across repos:
  - `~/.codex/templates/NOTES.md`
  - `~/.codex/templates/profile.yaml`
  - `~/.codex/templates/instructions.md`
- Order of precedence for templates: repo `.codex/templates/` > global `~/.codex/templates/` > embedded defaults.
