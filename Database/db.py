import sqlite3
import uuid


def init_db():
    conn = sqlite3.connect('booking.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS doctors 
                (id TEXT PRIMARY KEY, name TEXT, specialization TEXT, timings TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS appointments 
                (id TEXT PRIMARY KEY, doctor_id TEXT, patient_id TEXT, date TEXT, time TEXT,
                FOREIGN KEY(doctor_id) REFERENCES doctors(id))''')

    c.execute("INSERT OR IGNORE INTO doctors VALUES (?, ?, ?, ?)",
              (str(uuid.uuid4()), "Dr. Smith", "Cardiology", "9AM-5PM"))
    c.execute("INSERT OR IGNORE INTO doctors VALUES (?, ?, ?, ?)",
              (str(uuid.uuid4()), "Dr. Jones", "Neurology", "10AM-6PM"))
    conn.commit()
    conn.close()
