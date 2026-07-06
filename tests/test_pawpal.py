from pawpal_system import Owner, Pet, Task, Scheduler
from datetime import datetime

def test_mark_done_changes_status():
    task = Task("Walk", 30, "high", time="08:00", pet_name="Biscuit")
    task.mark_done()
    assert task.is_done == True

def test_add_task_increases_count():
    pet = Pet("Biscuit", "Dog", 3)
    task = Task("Walk", 30, "high", time="08:00", pet_name="Biscuit")
    pet.add_task(task)
    assert len(pet.get_tasks()) == 1

def test_sort_by_time():
    owner = Owner("Jordan", "j@email.com")
    pet = Pet("Biscuit", "Dog", 3)
    pet.add_task(Task("Evening walk", 30, "medium", time="18:00", pet_name="Biscuit"))
    pet.add_task(Task("Morning walk", 30, "high", time="08:00", pet_name="Biscuit"))
    owner.add_pet(pet)
    scheduler = Scheduler(owner=owner)
    sorted_tasks = scheduler.sort_by_time()
    assert sorted_tasks[0].time == "08:00"

def test_conflict_detection():
    owner = Owner("Jordan", "j@email.com")
    pet = Pet("Biscuit", "Dog", 3)
    pet.add_task(Task("Walk", 30, "high", time="09:00", pet_name="Biscuit"))
    pet.add_task(Task("Feeding", 10, "high", time="09:00", pet_name="Biscuit"))
    owner.add_pet(pet)
    scheduler = Scheduler(owner=owner)
    conflicts = scheduler.detect_conflicts()
    assert len(conflicts) > 0