"""
AgriTwin - Digital Twin Platform for Precision Farming and Crop Health Prediction
-----------------------------------------------------------------------------
A simple Flask web application that simulates farm sensor data (soil moisture,
temperature, humidity), applies basic rule-based prediction logic, and shows
irrigation and crop health status on a dashboard.

Author : <Your Name>
Course : <Your Course / Subject>
"""

import random
from datetime import datetime

from flask import Flask, render_template

app = Flask(__name__)


# ---------------------------------------------------------------------------
# Simulated Digital Twin - Sensor Data Generator
# ---------------------------------------------------------------------------
def generate_farm_data():
    """
    Simulates real-time sensor readings coming from IoT devices installed
    in a farm field (the 'physical twin'). In a real AgriTwin system this
    data would come from actual soil moisture probes, DHT22 sensors, etc.
    """
    data = {
        "soil_moisture": round(random.uniform(10, 60), 2),   # in %
        "temperature": round(random.uniform(15, 40), 2),     # in Celsius
        "humidity": round(random.uniform(20, 90), 2),        # in %
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    return data


# ---------------------------------------------------------------------------
# Prediction Logic (Digital Twin "Brain")
# ---------------------------------------------------------------------------
def predict_irrigation(soil_moisture):
    """Simple threshold-based irrigation prediction."""
    if soil_moisture < 30:
        return "Irrigation Needed", "danger"
    elif soil_moisture < 45:
        return "Monitor Soil Moisture", "warning"
    else:
        return "No Irrigation Needed", "success"


def predict_crop_health(soil_moisture, temperature, humidity):
    """
    Simple rule-based crop health classifier.
    Combines the three parameters to flag the crop as Healthy or At Risk.
    """
    risk_score = 0

    if soil_moisture < 30:
        risk_score += 1
    if temperature > 35 or temperature < 18:
        risk_score += 1
    if humidity < 30 or humidity > 80:
        risk_score += 1

    if risk_score >= 2:
        return "Risk", "danger"
    elif risk_score == 1:
        return "Moderate Risk", "warning"
    else:
        return "Healthy", "success"


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------
@app.route("/")
def dashboard():
    farm_data = generate_farm_data()

    irrigation_status, irrigation_level = predict_irrigation(
        farm_data["soil_moisture"]
    )
    health_status, health_level = predict_crop_health(
        farm_data["soil_moisture"],
        farm_data["temperature"],
        farm_data["humidity"],
    )

    return render_template(
        "index.html",
        farm_data=farm_data,
        irrigation_status=irrigation_status,
        irrigation_level=irrigation_level,
        health_status=health_status,
        health_level=health_level,
    )


if __name__ == "__main__":
    # host=0.0.0.0 is required so the app is reachable from outside
    # the Docker container.
    app.run(host="0.0.0.0", port=5000, debug=True)
