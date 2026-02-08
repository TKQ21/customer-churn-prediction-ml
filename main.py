"""
Project: Customer Churn Prediction
Author: Mohd Kaif
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Dummy dataset
data = {
    "age": [25, 30, 45, 35, 50],
    "salary": [40000, 50000, 80000, 60000, 90000],
    "churn": [0, 1, 0, 1, 0]
}

df = pd.DataFrame(data)

X = df[["age", "salary"]]
y = df["churn"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LogisticRegression()
model.fit(X_train, y_train)

print("Model trained successfully")
