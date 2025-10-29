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

