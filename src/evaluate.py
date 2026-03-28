# Assisted by ChatGPT
import pandas as pd
import joblib
from sklearn.metrics import mean_squared_error
import json
import os

X_test = pd.read_csv("data/features/X_test.csv")
y_test = pd.read_csv("data/features/y_test.csv")

model = joblib.load("models/model.pkl")

preds = model.predict(X_test)

mse = mean_squared_error(y_test, preds)

metrics = {"mse": mse}

os.makedirs("reports", exist_ok=True)

with open("reports/metrics.json", "w") as f:
    json.dump(metrics, f)