import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from fairlearn.metrics import MetricFrame

df = pd.read_csv("data.csv")

df["target"] = df["target"].map({"yes":1,"no":0})

X = df.drop(columns=["target","sno"])
y = df["target"]

X_train, X_test, y_train, y_test = train_test_split(
X,
y,
test_size=0.2,
random_state=42
)

model = joblib.load("models/model.pkl")

pred = model.predict(X_test)

mf = MetricFrame(
metrics=accuracy_score,
y_true=y_test,
y_pred=pred,
sensitive_features=X_test["age"]
)

print(mf.by_group)

