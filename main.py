from fastapi import FastAPI, HTTPException, Query
from typing import List, Optional
from Models.models import Doctor, Appointment, AppointmentCreate
from Services.services import DoctorService, AppointmentService
from Database.db import init_db
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(title="Doctor-Patient Booking API", lifespan=lifespan)


@app.get("/doctors", response_model=List[Doctor])
async def get_doctors():
    doctor_service = DoctorService()
    return doctor_service.get_all_doctors()


@app.get("/doctors/{id}", response_model=Doctor)
async def get_doctor(id: str):
    doctor_service = DoctorService()
    doctor = doctor_service.get_doctor_by_id(id)
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return doctor


@app.post("/appointments", response_model=Appointment, status_code=201)
async def create_appointment(appointment: AppointmentCreate):
    appointment_service = AppointmentService()
    return appointment_service.create_appointment(appointment)


@app.get("/appointments", response_model=List[Appointment])
async def get_appointments(
    doctor_id: Optional[str] = Query(None),
    patient_id: Optional[str] = Query(None)
):
    if not doctor_id and not patient_id:
        raise HTTPException(
            status_code=400, detail="Either doctor_id or patient_id must be provided")

    appointment_service = AppointmentService()
    if doctor_id:
        return appointment_service.get_appointments_by_doctor(doctor_id)
    if patient_id is not None:
        return appointment_service.get_appointments_by_patient(patient_id)
    else:
        raise HTTPException(
            status_code=400, detail="patient_id must be provided")
