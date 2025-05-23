# EV Fault Detection System

A Raspberry Pi + AI project for real-time fault detection in EV service centers.

## Features
- Simulated or real sensor data
- AI model to predict EV faults
- Web dashboard (Flask)
- Optional hardware buzzer alert (Raspberry Pi)

## How to Run
1. `python scripts/train_model.py`
2. Run sensor: `python scripts/simulate_sensor.py`
3. Start server: `python app/main.py`

## Hardware (optional)
- Raspberry Pi
- Buzzer (GPIO 18)
- Sensors (DHT11, INA219, etc.)
