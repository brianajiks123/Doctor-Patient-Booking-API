FROM python:3.13.5-alpine

WORKDIR /app

COPY main.py .
COPY Models /app/Models
COPY Services /app/Services
COPY Database /app/Database
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
