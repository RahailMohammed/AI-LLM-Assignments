# Assisted by ChatGPT
import pandas as pd
import joblib
import os
from sklearn.linear_model import LinearRegression

X_train = pd.read_csv("data/features/X_train.csv")
y_train = pd.read_csv("data/features/y_train.csv")

model = LinearRegression()
model.fit(X_train, y_train)

os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/model.pkl")