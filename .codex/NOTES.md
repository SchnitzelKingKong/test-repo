Project Summary
- One-liner: Exercises and notes for an ML course (TensorFlow, Kaggle, DS).
- Scope: Weekly notebooks, small scripts, and learning artifacts under `KW43/`.

Current Objective
- Build and train a simple Keras regression model (housing prices).

Key Decisions / Constraints
- Language: English primary, German fallback.
- Libraries: TensorFlow/Keras; WatsonxLLM and crewai experiments in `_misc/`.
- Data: Jupyter notebooks inside `KW43/tensorflow/` and `kaggle_python/`.
- Environment: Local workspace-write; network restricted within this CLI.

Status
- Done: Notebook scaffolded; `model.compile(optimizer='adam', loss='mse', metrics=['mae'])` in place.
- Blocked: Need to confirm dataset loading/preprocessing for housing prices.

Open Tasks
- [ ] Verify dataset path and train/val/test split; avoid leakage.
- [ ] Fit model and plot learning curves (loss/MAE).
- [ ] Experiment with learning rate and batch size; note results.
- [ ] Review `agent.py` syntax issues (typos, imports) if used.

Pointers
- Files: `KW43/tensorflow/Week1_Notebook1_Housing_Prices.ipynb:Cell 9` (compile + summary)
- Files: `KW43/_misc/agent.py:23` (Agent constructor block)
- Notes: `KW43/tensorflow/preperation-kw43.md` (loss/backprop/training notes)

Decisions Log
- 2025-10-28 — Added .codex structure for portable context across chats.
- 2025-10-28 — Fashion MNIST low eval accuracy traced to two issues: (1) loss set with `from_logits=True` while final layer uses `softmax`; (2) training on unnormalized `X_train` but evaluating on normalized `x_test`. Plan: set `from_logits=False` or remove softmax; consistently use normalized data for both train/eval.

Next Steps
- Load data, normalize features, fit model; record metrics in NOTES.
- Fix compile loss/logits mismatch; retrain and re-evaluate; log new train/val/test accuracy.
