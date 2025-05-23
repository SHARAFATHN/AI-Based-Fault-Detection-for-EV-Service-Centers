import json, joblib

def predict_fault():
    with open("../data/realtime_data.json") as f:
        data = json.load(f)
    model = joblib.load("../model/fault_model.pkl")
    input_data = [[data[k] for k in ['temperature', 'vibration', 'voltage', 'current']]]
    pred = model.predict(input_data)[0]
    return pred, data
