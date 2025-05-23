import random, time, json

def simulate_sensor_data():
    return {
        'temperature': random.uniform(30, 90),
        'vibration': random.uniform(0.1, 2.0),
        'voltage': random.uniform(12, 14.5),
        'current': random.uniform(0, 100)
    }

while True:
    data = simulate_sensor_data()
    with open("../data/realtime_data.json", "w") as f:
        json.dump(data, f)
    print("Simulated data:", data)
    time.sleep(5)
