FROM python:3.11-slim AS build-stage

WORKDIR /home/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["fastapi", "run", "app/main.py", "--port", "8000", "--host", "0.0.0.0"]