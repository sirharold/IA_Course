## Copilot instructions for this workspace

You are working on a small legacy reconciliation service used for training.

### Primary goals

- Understand the current behavior before suggesting changes.
- Prefer explanations backed by code, data, logs, or SQL evidence.
- Keep changes small, reversible, and easy to verify.
- Distinguish clearly between facts, inferences, and open questions.

### When analyzing code

- Cite specific files and functions.
- Call out hidden data assumptions, not just code structure.
- Avoid proposing large refactors unless the user explicitly asks for them.

### When analyzing incidents

- Separate symptom, probable cause, alternative cause, and missing evidence.
- Prefer giving two hypotheses over pretending certainty.

### When proposing tests

- Derive tests from observed risks, logs, or malformed data.
- Separate base cases, edge cases, and error cases.

### When working with SQL

- Explain what the query is trying to validate before writing it.
- Prefer SELECT first, then propose UPDATE or DELETE only after showing the impact.
- If proposing a data fix, include a safe preview query.
