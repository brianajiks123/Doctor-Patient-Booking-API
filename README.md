# Docter-Patient Booking API

## Screenshots

![Docker Run](Docs/Docker%20Run.png)
![API Endpoints: /doctors](Docs/GET%20doctors.png)
![API Endpoints: /doctors/:id](Docs/GET%20doctors%20by%20id.png)

## Features

- List all doctors (name, specialization, timings)
- Get doctor details by id
- View all appointments by doctor or patient id
- Book an appointment (with date, time, doctor_id, patient_id)

## Installation

1. Clone the repository: `git clone https://github.com/brianajiks123/Doctor-Patient-Booking-API.git`
2. Move into the project directory: `cd Doctor-Patient-Booking-API`
3. Install dependencies: `pip install -r requirements.txt`

## Usage

1. Build the docker image: `docker build -t doctor-patient-api .`
2. Run the docker container: `docker run --name doctor-patient-api -p 38000:8000 doctor-patient-api`
3. Interact with the API using tools like Postman or cURL

## API Endpoints

### Doctors

- `GET /doctors`: List all doctors
- `GET /doctors/:id`: Get doctor details by id

### Appointments

- `GET /appointments?doctor_id=`: View all appointments for a doctor
- `GET /appointments?patient_id=`: View all appointments for a patient
- `POST /appointments`: Book an appointment

## Tools

- [Python 3.13.5](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Pydantic](https://pydantic-docs.helpmanual.io/)
- [Uvicorn](https://www.starlette.io/)
- [SQLite](https://www.sqlite.org/index.html)
- [Docker](https://www.docker.com/)
