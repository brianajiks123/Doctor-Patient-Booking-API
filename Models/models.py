from pydantic import BaseModel


class Doctor(BaseModel):
    id: str
    name: str
    specialization: str
    timings: str


class Appointment(BaseModel):
    id: str
    doctor_id: str
    patient_id: str
    date: str
    time: str


class AppointmentCreate(BaseModel):
    doctor_id: str
    patient_id: str
    date: str
    time: str
