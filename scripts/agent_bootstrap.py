#!/usr/bin/env python3
"""
Single-file Agent Bootstrap

Purpose
- Ensure a consistent startup flow for agents with zero repo-specific changes:
  1) Detect `.codex/` context.
  2) If missing, scaffold from global templates at `~/.codex/templates/` (or embedded defaults).
  3) Expose resolved paths to NOTES and profile for the agent to load.

Usage
- Agents/tools: run `python scripts/agent_bootstrap.py` (optionally `--force` to overwrite).
"""
from __future__ import annotations
import os
import sys
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CODEX_DIR = ROOT / ".codex"
TEMPLATES_REPO = CODEX_DIR / "templates"
TEMPLATES_GLOBAL = Path(os.path.expanduser("~/.codex/templates"))

DEFAULTS = {
    "NOTES.md": """
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
""".strip(),
    "profile.yaml": """
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
""".strip(),
    "instructions.md": """
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
""".strip(),
}


def choose_template(name: str) -> Path | None:
    """Pick template file by precedence: repo > global > None."""
    repo_path = TEMPLATES_REPO / name
    if repo_path.is_file():
        return repo_path
    global_path = TEMPLATES_GLOBAL / name
    if global_path.is_file():
        return global_path
    return None


def write_if_needed(path: Path, content: str, force: bool) -> bool:
    if path.exists() and not force:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return True


def scaffold(force: bool = False) -> None:
    CODEX_DIR.mkdir(parents=True, exist_ok=True)

    created = []
    for name in ("NOTES.md", "profile.yaml", "instructions.md"):
        tpl = choose_template(name)
        target = CODEX_DIR / name
        if tpl is not None:
            if target.exists() and not force:
                continue
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(tpl, target)
            created.append(str(target))
        else:
            if write_if_needed(target, DEFAULTS[name], force):
                created.append(str(target))

    if created:
        print("created:")
        for p in created:
            print(f"- {p}")
    else:
        print("no changes (existing files kept)")


def main(argv: list[str]) -> int:
    force = "--force" in argv
    if not CODEX_DIR.exists() or force:
        scaffold(force=force)
    # Output resolved pointers for agents to consume
    notes = CODEX_DIR / "NOTES.md"
    profile = CODEX_DIR / "profile.yaml"
    instructions = CODEX_DIR / "instructions.md"
    print("resolved:")
    print(f"NOTES={notes}")
    print(f"PROFILE={profile}")
    print(f"INSTRUCTIONS={instructions}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

