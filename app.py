import streamlit as st
from db import Database
from models import Reminder

db = Database()
st.title("⏰ Reminder App")

menu = ["Add Reminder", "View Reminders", "Manage Reminders"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Add Reminder":
    st.subheader("Add New Reminder")
    title = st.text_input("Title")
    description = st.text_area("Description")
    date = st.date_input("Date")
    time = st.time_input("Time")

    if st.button("Add Reminder"):
        reminder = Reminder(title=title, description=description, date=str(date), time=str(time))
        db.add_reminder(reminder)
        st.success(f"Reminder '{title}' added successfully!")

elif choice == "View Reminders":
    st.subheader("All Reminders")
    reminders = db.get_all()
    if reminders:
        st.table(reminders)
    else:
        st.info("No reminders found.")

elif choice == "Manage Reminders":
    st.subheader("Update or Delete Reminders")
    reminders = db.get_all()
    if reminders:
        ids = [r[0] for r in reminders]
        selected = st.selectbox("Select Reminder ID", ids)

        if st.button("Mark as Done"):
            db.mark_done(selected)
            st.success("Marked as done!")
        if st.button("Delete Reminder"):
            db.delete(selected)
            st.warning("Reminder deleted.")
    else:
        st.info("No reminders to manage.")
