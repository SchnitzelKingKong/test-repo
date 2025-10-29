Using .codex for Context

- Maintain session context in `.codex/NOTES.md` (goals, decisions, status, open tasks, pointers).
- Capture preferences in `.codex/profile.yaml` (language, tone, workflow patterns).
- At the start of any new chat, reference these files by path so I can instantly regain context.

Suggested Workflow
- After meaningful changes, update the relevant sections in NOTES.md.
- Log important decisions with date and rationale.
- Point to exact files and lines instead of pasting large chunks.

Quick Bootstrap Template (paste in new chat)
```
Context bootstrap
- Project: <one-liner>
- Current objective: <short>
- Key decisions: see .codex/NOTES.md (Decisions Log)
- Pointers: see .codex/NOTES.md (Pointers)
- Constraints: <env, versions, sandbox>
- Next steps: <1–3 items>
```

