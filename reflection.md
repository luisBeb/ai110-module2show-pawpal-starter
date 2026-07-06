# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

I designed four classes: Owner, Pet, Task, and Scheduler. Owner holds the owner's name and email and manages a list of pets. Pet stores the animal's name, species, and age, and holds a list of tasks. Task represents a single care activity with a title, duration, priority, scheduled time, and a recurring flag. Scheduler is the brain — it retrieves all tasks from the owner's pets, sorts them by time, filters them, and detects conflicts.

**b. Design changes**

During implementation I added a `time` field (HH:MM string) to Task instead of relying solely on `due_date`. This made sorting and conflict detection much simpler since comparing time strings directly is straightforward in Python.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

The scheduler considers three constraints: time (tasks are sorted chronologically by HH:MM), priority (labeled low, medium, or high so the owner knows what matters most), and conflicts (two tasks at the exact same time are flagged). I prioritized time-based sorting first because a daily schedule needs to be chronological to be useful.

**b. Tradeoffs**

One tradeoff is that conflict detection only checks for exact time matches, not overlapping durations. A 30-minute task at 08:00 and a task at 08:15 would not be flagged even though they overlap. This keeps the logic simple and readable, but a more complete system would calculate end times and check for overlaps.

---

## 3. AI Collaboration

**a. How you used AI**

I used AI throughout the project for system design brainstorming, generating class skeletons from UML, implementing scheduling logic, writing pytest test cases, and debugging. The most helpful prompts were specific ones that included context, like sharing the current file and asking for a targeted improvement.

**b. Judgment and verification**

When AI generated the conflict detection logic, I reviewed it carefully and verified it worked by intentionally adding two tasks at the same time in main.py and confirming the warning printed correctly. I also ran all four pytest tests to verify behavior before committing.

---

## 4. Testing and Verification

**a. What you tested**

I tested four behaviors: marking a task done changes its status, adding a task to a pet increases the task count, sorting tasks returns them in chronological order, and conflict detection flags duplicate times.

**b. Confidence**

I am confident the core scheduling logic works correctly for the tested cases. Edge cases I would test next include a pet with no tasks, tasks with identical titles at different times, and weekly recurring tasks rolling over correctly.

---

## 5. Reflection

**a. What went well**

The CLI-first workflow worked really well. Running main.py before connecting to Streamlit let me verify the logic was correct before worrying about the UI.

**b. What you would improve**

I would improve conflict detection to check for overlapping durations rather than just exact time matches. I would also add the ability to edit or delete tasks from the Streamlit UI.

**c. Key takeaway**

The most important thing I learned is that designing the system on paper first (UML) before writing any code makes implementation much smoother. AI is a powerful collaborator but the human still needs to review and verify every suggestion.