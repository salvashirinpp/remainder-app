import sqlite3
from models import Reminder

class Database:
    def __init__(self, db_name="reminders.db"):
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS reminders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            description TEXT,
            date TEXT,
            time TEXT,
            status TEXT
        )
        """
        self.conn.execute(query)
        self.conn.commit()

    def add_reminder(self, reminder: Reminder):
        query = "INSERT INTO reminders (title, description, date, time, status) VALUES (?, ?, ?, ?, ?)"
        self.conn.execute(query, (reminder.title, reminder.description, reminder.date, reminder.time, reminder.status))
        self.conn.commit()

    def get_all(self):
        cursor = self.conn.execute("SELECT * FROM reminders ORDER BY date, time")
        return cursor.fetchall()

    def mark_done(self, reminder_id):
        self.conn.execute("UPDATE reminders SET status='Done' WHERE id=?", (reminder_id,))
        self.conn.commit()

    def delete(self, reminder_id):
        self.conn.execute("DELETE FROM reminders WHERE id=?", (reminder_id,))
        self.conn.commit()
    