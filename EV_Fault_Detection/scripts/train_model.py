import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Simulate data
df = pd.DataFrame({
    'temperature': [60, 85, 90, 70, 45],
    'vibration': [0.3, 1.8, 2.1, 0.5, 0.2],
    'voltage': [13.0, 12.4, 11.5, 13.5, 14.2],
    'current': [50, 80, 95, 45, 20],
    'fault': [0, 1, 1, 0, 0]
})

X = df.drop('fault', axis=1)
y = df['fault']
model = RandomForestClassifier()
model.fit(X, y)
joblib.dump(model, '../model/fault_model.pkl')
