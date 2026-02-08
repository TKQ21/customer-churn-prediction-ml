"""
Customer Churn Prediction
Author: Mohd Kaif

This project demonstrates a basic machine learning workflow
for predicting customer churn. The implementation focuses on
understanding data preprocessing, model training, and evaluation.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Sample dataset (illustrative)
data = {
    "tenure": [1, 12, 24, 36, 48, 60],
    "monthly_charges": [30, 45, 60, 70, 80, 90],
    "churn": [1, 1, 0, 0, 0, 0]
}

df = pd.DataFrame(data)

X = df[["tenure", "monthly_charges"]]
y = df["churn"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

model = LogisticRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

print(f"Model trained successfully. Accuracy: {accuracy:.2f}")
