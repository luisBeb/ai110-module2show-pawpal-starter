# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

I designed four classes:
- **Owner**: holds the owner's name and email, and a list of their pets. Can add pets and retrieve them.
- **Pet**: holds the pet's name, species, and age, and a reference to its owner.
- **Task**: represents a care task (walk, feeding, etc.) with a title, duration, priority, due date, and a recurring flag. Can mark itself done and check if it's due today.
- **Scheduler**: holds a list of tasks and handles adding tasks, retrieving today's tasks, sorting by priority, and detecting conflicts.

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

The scheduler considers three constraints:
- **Time**: tasks are sorted by their HH:MM scheduled time using `sort_by_time()`
- **Priority**: tasks are labeled low, medium, or high to help the owner know what matters most
- **Conflicts**: the scheduler detects if two tasks are scheduled at the exact same time using `detect_conflicts()`

I prioritized time-based sorting first because a daily schedule needs to be chronological to be useful.

**b. Tradeoffs**

One tradeoff is that conflict detection only checks for exact time matches, not overlapping durations. For example, a 30-minute task at 08:00 and a task at 08:15 would not be flagged as a conflict even though they overlap. This keeps the logic simple and readable, but a more complete system would calculate end times and check for overlaps.

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
