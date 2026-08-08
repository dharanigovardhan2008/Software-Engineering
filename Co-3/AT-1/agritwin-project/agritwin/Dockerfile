# -----------------------------------------------------------------------
# AgriTwin - Dockerfile
# Base image: lightweight official Python image
# -----------------------------------------------------------------------
FROM python:3.11-slim

# Set metadata (optional but good practice)
LABEL maintainer="AgriTwin Team"
LABEL description="Digital Twin Platform for Precision Farming and Crop Health Prediction"

# Set working directory inside the container
WORKDIR /app

# Copy only requirements first (Docker layer caching optimization)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application source code
COPY . .

# Inform Docker that the container listens on port 5000
EXPOSE 5000

# Environment variables for Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Command to run the application
CMD ["python", "app.py"]
