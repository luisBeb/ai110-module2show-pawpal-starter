import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")
st.title("🐾 PawPal+")

# --- Session State Setup ---
if "owner" not in st.session_state:
    st.session_state.owner = None

# --- Owner & Pet Info ---
st.header("👤 Owner & Pet Info")

owner_name = st.text_input("Owner name", value="Jordan")
owner_email = st.text_input("Owner email", value="jordan@email.com")

pet_name = st.text_input("Pet name", value="Biscuit")
species = st.selectbox("Species", ["dog", "cat", "other"])
age = st.number_input("Pet age", min_value=0, max_value=30, value=3)

if st.button("Save Owner & Pet"):
    pet = Pet(name=pet_name, species=species, age=age)
    owner = Owner(name=owner_name, email=owner_email)
    owner.add_pet(pet)
    st.session_state.owner = owner
    st.success(f"Saved! Owner: {owner_name}, Pet: {pet_name}")

st.divider()

# --- Add Tasks ---
st.header("📋 Add a Task")

if st.session_state.owner:
    pets = st.session_state.owner.get_pets()
    pet_names = [p.name for p in pets]
    selected_pet = st.selectbox("Assign to pet", pet_names)

    task_title = st.text_input("Task title", value="Morning walk")
    duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=30)
    priority = st.selectbox("Priority", ["low", "medium", "high"], index=2)
    time = st.text_input("Time (HH:MM)", value="08:00")
    recurring = st.selectbox("Recurring", ["none", "daily", "weekly"])

    if st.button("Add Task"):
        for pet in pets:
            if pet.name == selected_pet:
                task = Task(
                    title=task_title,
                    duration_minutes=int(duration),
                    priority=priority,
                    time=time,
                    pet_name=selected_pet,
                    recurring=recurring
                )
                pet.add_task(task)
                st.success(f"Task '{task_title}' added to {selected_pet}!")
else:
    st.info("Please save an owner and pet first.")

st.divider()

# --- Generate Schedule ---
st.header("📅 Today's Schedule")

if st.button("Generate Schedule"):
    if st.session_state.owner:
        scheduler = Scheduler(owner=st.session_state.owner)
        plan, conflicts = scheduler.generate_plan()

        if plan:
            for task in plan:
                status = "✅" if task.is_done else "🔲"
                st.write(f"{status} **{task.time}** — {task.title} ({task.duration_minutes} min) [{task.priority}] - {task.pet_name}")
        else:
            st.info("No tasks scheduled yet.")

        if conflicts:
            st.subheader("⚠️ Conflicts Detected")
            for c in conflicts:
                st.warning(c)
    else:
        st.error("Please save an owner and pet first.")