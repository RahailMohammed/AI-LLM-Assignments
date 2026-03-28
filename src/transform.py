# Assisted by ChatGPT
import pandas as pd
from sklearn.preprocessing import StandardScaler
import os

train = pd.read_csv("data/processed/train.csv")
test = pd.read_csv("data/processed/test.csv")

target = "price"

X_train = train.drop(columns=[target])
y_train = train[target]

X_test = test.drop(columns=[target])
y_test = test[target]

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

os.makedirs("data/features", exist_ok=True)

pd.DataFrame(X_train_scaled).to_csv("data/features/X_train.csv", index=False)
pd.DataFrame(X_test_scaled).to_csv("data/features/X_test.csv", index=False)
y_train.to_csv("data/features/y_train.csv", index=False)
y_test.to_csv("data/features/y_test.csv", index=False)