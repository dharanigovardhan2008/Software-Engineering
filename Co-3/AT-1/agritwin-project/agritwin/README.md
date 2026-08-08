# 🌾 AgriTwin – Digital Twin Platform for Precision Farming and Crop Health Prediction

AgriTwin is a simple Flask-based web application that simulates a **digital
twin** of a farm field. It generates mock IoT sensor data (soil moisture,
temperature, humidity), applies basic rule-based prediction logic, and
displays irrigation recommendations and crop health status on a dashboard.

## Features
- Simulated real-time farm sensor data
- Rule-based irrigation prediction (`Irrigation Needed` / `Monitor` / `No Irrigation Needed`)
- Rule-based crop health classification (`Healthy` / `Moderate Risk` / `Risk`)
- Clean, responsive dashboard UI
- Fully Dockerized for easy deployment

## Tech Stack
- Python 3.11 + Flask
- HTML5 / CSS3 (Jinja2 templating)
- Docker & Docker Compose

## Run Locally (without Docker)
```bash
pip install -r requirements.txt
python app.py
```
Visit: http://127.0.0.1:5000

## Run with Docker
```bash
docker build -t agritwin-app .
docker run -p 5000:5000 agritwin-app
```

## Run with Docker Compose
```bash
docker-compose up --build
```
Visit: http://localhost:5000

## Project Structure
```
agritwin/
├── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .gitignore
├── README.md
└── templates/
    └── index.html
```

## License
This project is created for academic/educational purposes.
