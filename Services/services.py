from typing import List, Optional
import sqlite3
from datetime import datetime
import uuid
from Models.models import Doctor, Appointment, AppointmentCreate
from fastapi import HTTPException


class DoctorService:
    def __init__(self):
        self.cache = {}

    def get_all_doctors(self) -> List[Doctor]:
        if 'doctors' in self.cache:
            return self.cache['doctors']

        conn = sqlite3.connect('booking.db')
        c = conn.cursor()
        c.execute("SELECT * FROM doctors")
        doctors = [Doctor(id=row[0], name=row[1], specialization=row[2],
                          timings=row[3]) for row in c.fetchall()]
        conn.close()

        self.cache['doctors'] = doctors
        return doctors

    def get_doctor_by_id(self, doctor_id: str) -> Optional[Doctor]:
        conn = sqlite3.connect('booking.db')
        c = conn.cursor()
        c.execute("SELECT * FROM doctors WHERE id = ?", (doctor_id,))
        row = c.fetchone()
        conn.close()

        if row:
            return Doctor(id=row[0], name=row[1], specialization=row[2], timings=row[3])
        return None


class AppointmentService:
    def create_appointment(self, appointment: AppointmentCreate) -> Appointment:
        try:
            datetime.strptime(appointment.date, '%Y-%m-%d')
            datetime.strptime(appointment.time, '%H:%M')
        except ValueError:
            raise HTTPException(
                status_code=400, detail="Invalid date or time format. Use YYYY-MM-DD and HH:MM")

        doctor_service = DoctorService()
        if not doctor_service.get_doctor_by_id(appointment.doctor_id):
            raise HTTPException(status_code=404, detail="Doctor not found")

        conn = sqlite3.connect('booking.db')
        c = conn.cursor()
        c.execute("SELECT * FROM appointments WHERE doctor_id = ? AND date = ? AND time = ?",
                  (appointment.doctor_id, appointment.date, appointment.time))
        if c.fetchone():
            conn.close()
            raise HTTPException(
                status_code=400, detail="Appointment slot already taken")

        appointment_id = str(uuid.uuid4())
        c.execute("INSERT INTO appointments VALUES (?, ?, ?, ?, ?)",
                  (appointment_id, appointment.doctor_id, appointment.patient_id,
                   appointment.date, appointment.time))
        conn.commit()
        conn.close()

        return Appointment(
            id=appointment_id,
            doctor_id=appointment.doctor_id,
            patient_id=appointment.patient_id,
            date=appointment.date,
            time=appointment.time
        )

    def get_appointments_by_doctor(self, doctor_id: str) -> List[Appointment]:
        conn = sqlite3.connect('booking.db')
        c = conn.cursor()
        c.execute("SELECT * FROM appointments WHERE doctor_id = ?", (doctor_id,))
        appointments = [Appointment(
            id=row[0], doctor_id=row[1], patient_id=row[2], date=row[3], time=row[4]) for row in c.fetchall()]
        conn.close()
        return appointments

    def get_appointments_by_patient(self, patient_id: str) -> List[Appointment]:
        conn = sqlite3.connect('booking.db')
        c = conn.cursor()
        c.execute("SELECT * FROM appointments WHERE patient_id = ?", (patient_id,))
        appointments = [Appointment(
            id=row[0], doctor_id=row[1], patient_id=row[2], date=row[3], time=row[4]) for row in c.fetchall()]
        conn.close()
        return appointments
