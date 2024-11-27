import pickle

import pandas as pd
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    input_data = pd.DataFrame(
        {
            # request these from the form
            "MonthlyCharges": [float(request.form["MonthlyCharges"])],
            "TotalCharges": [float(request.form["TotalCharges"])],
            "tenure": [int(request.form["tenure"])],
            # making static to reduce complexity from user side
            "gender": ["Male"],
            "SeniorCitizen": [0],
            "Partner": ["Yes"],
            "Dependents": ["No"],
            "PhoneService": ["Yes"],
            "MultipleLines": ["No phone service"],
            "InternetService": ["DSL"],
            "OnlineSecurity": ["No"],
            "OnlineBackup": ["Yes"],
            "DeviceProtection": ["No"],
            "TechSupport": ["No"],
            "StreamingTV": ["No"],
            "StreamingMovies": ["No"],
            "Contract": ["One year"],
            "PaperlessBilling": ["Yes"],
            "PaymentMethod": ["Bank transfer (automatic)"],
        }
    )
    result = run_model(input_data)

    if result:
        return jsonify({"prediction": "Customer Will Churn"})
    else:
        return jsonify({"prediction": "Customer Will Not Churn"})


def run_model(data: pd.DataFrame) -> int:

    with open("model.pkl", "rb") as file:
        model = pickle.load(file)

    prediction = model.predict(data)
    return prediction[0]


if __name__ == "__main__":
    app.run()
