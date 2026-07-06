from pawpal_system import Owner, Pet, Task, Scheduler
from datetime import datetime

# Setup
owner = Owner(name="Jordan", email="jordan@email.com")

dog = Pet(name="Biscuit", species="Golden Retriever", age=3)
cat = Pet(name="Mochi", species="Cat", age=2)

# Add tasks to dog
dog.add_task(Task("Morning walk", 30, "high", time="08:00", pet_name="Biscuit"))
dog.add_task(Task("Feeding", 10, "high", time="09:00", pet_name="Biscuit"))
dog.add_task(Task("Evening walk", 30, "medium", time="18:00", pet_name="Biscuit"))

# Add tasks to cat
cat.add_task(Task("Feeding", 5, "high", time="09:00", pet_name="Mochi"))  # conflict!
cat.add_task(Task("Grooming", 15, "low", time="14:00", pet_name="Mochi"))

owner.add_pet(dog)
owner.add_pet(cat)

scheduler = Scheduler(owner=owner)
plan, conflicts = scheduler.generate_plan()

print("\n🐾 Today's Schedule:")
print("-" * 40)
for task in plan:
    status = "✅" if task.is_done else "🔲"
    print(f"{status} {task.time} — {task.title} ({task.duration_minutes} min) [{task.priority}] - {task.pet_name}")

if conflicts:
    print("\n⚠️ Conflicts Detected:")
    for c in conflicts:
        print(c)