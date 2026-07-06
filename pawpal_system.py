from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import List, Optional

@dataclass
class Task:
    """Represents a single pet care activity."""
    title: str
    duration_minutes: int
    priority: str  # "low", "medium", "high"
    time: str = "08:00"  # HH:MM format
    pet_name: str = ""
    is_done: bool = False
    recurring: str = "none"  # "none", "daily", "weekly"
    due_date: datetime = field(default_factory=datetime.today)

    def mark_done(self):
        """Mark this task as complete."""
        self.is_done = True
        if self.recurring == "daily":
            self.due_date = datetime.today() + timedelta(days=1)
        elif self.recurring == "weekly":
            self.due_date = datetime.today() + timedelta(weeks=1)

    def is_due_today(self):
        """Check if this task is due today."""
        return self.due_date.date() == datetime.today().date()


@dataclass
class Pet:
    """Stores pet details and a list of tasks."""
    name: str
    species: str
    age: int
    tasks: List = field(default_factory=list)

    def add_task(self, task: Task):
        """Add a task to this pet."""
        self.tasks.append(task)

    def get_tasks(self):
        """Return all tasks for this pet."""
        return self.tasks


@dataclass
class Owner:
    """Manages multiple pets and provides access to all their tasks."""
    name: str
    email: str
    pets: List = field(default_factory=list)

    def add_pet(self, pet: Pet):
        """Add a pet to this owner."""
        self.pets.append(pet)

    def get_pets(self):
        """Return all pets."""
        return self.pets

    def get_all_tasks(self):
        """Return all tasks across all pets."""
        all_tasks = []
        for pet in self.pets:
            all_tasks.extend(pet.get_tasks())
        return all_tasks


@dataclass
class Scheduler:
    """The brain that retrieves, organizes, and manages tasks across pets."""
    owner: Owner

    def get_all_tasks(self):
        """Get all tasks from all pets."""
        return self.owner.get_all_tasks()

    def sort_by_time(self):
        """Sort all tasks by their scheduled time (HH:MM)."""
        tasks = self.get_all_tasks()
        return sorted(tasks, key=lambda t: t.time)

    def filter_tasks(self, pet_name=None, done=None):
        """Filter tasks by pet name or completion status."""
        tasks = self.get_all_tasks()
        if pet_name:
            tasks = [t for t in tasks if t.pet_name == pet_name]
        if done is not None:
            tasks = [t for t in tasks if t.is_done == done]
        return tasks

    def detect_conflicts(self):
        """Return warning messages for tasks scheduled at the same time."""
        tasks = self.get_all_tasks()
        seen = {}
        conflicts = []
        for task in tasks:
            if task.time in seen:
                conflicts.append(
                    f"⚠️ Conflict at {task.time}: '{seen[task.time]}' and '{task.title}'"
                )
            else:
                seen[task.time] = task.title
        return conflicts

    def generate_plan(self):
        """Generate a sorted daily plan with conflict warnings."""
        sorted_tasks = self.sort_by_time()
        conflicts = self.detect_conflicts()
        return sorted_tasks, conflicts