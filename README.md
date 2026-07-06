# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

\```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
\```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## 🖥️ Sample Output

\```
🐾 Today's Schedule:
----------------------------------------
🔲 08:00 — Morning walk (30 min) [high] - Biscuit
🔲 09:00 — Feeding (10 min) [high] - Biscuit
🔲 09:00 — Feeding (5 min) [high] - Mochi
🔲 14:00 — Grooming (15 min) [low] - Mochi
🔲 18:00 — Evening walk (30 min) [medium] - Biscuit

⚠️ Conflicts Detected:
⚠️ Conflict at 09:00: 'Feeding' and 'Feeding'
\```

## 🧪 Testing PawPal+

\```bash
# Run the full test suite:
python -m pytest

# Run with coverage:
pytest --cov
\```

Sample test output:

\```
platform win32 -- Python 3.14.0, pytest-9.1.1
collected 4 items

tests\test_pawpal.py ....  [100%]

4 passed in 0.51s
\```

## 📐 Smarter Scheduling

| Feature | Method(s) | Notes |
|---------|-----------|-------|
| Task sorting | `Scheduler.sort_by_time()` | Sorts tasks by HH:MM string |
| Filtering | `Scheduler.filter_tasks()` | Filter by pet name or completion status |
| Conflict handling | `Scheduler.detect_conflicts()` | Flags tasks scheduled at the exact same time |
| Recurring tasks | `Task.mark_done()` | Advances due_date by 1 day (daily) or 7 days (weekly) |

## 📸 Demo Walkthrough

1. Enter your name and email in the Owner & Pet Info section.
2. Enter your pet's name, species, and age, then click **Save Owner & Pet**.
3. In the Add a Task section, fill in the task title, duration, priority, time, and recurrence, then click **Add Task**.
4. Repeat step 3 to add more tasks for your pet.
5. Click **Generate Schedule** to view today's sorted plan and any conflict warnings.