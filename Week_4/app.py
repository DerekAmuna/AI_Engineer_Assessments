import pickle
import pandas as pd
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        input_data = pd.DataFrame(
            {
                "MonthlyCharges": [float(request.form["MonthlyCharges"])],
                "TotalCharges": [float(request.form["TotalCharges"])],
                "tenure": [int(request.form["tenure"])],
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
    except (ValueError, TypeError) as e:
        return jsonify({"error": str(e)}), 500


def run_model(data: pd.DataFrame) -> int:
    try:
        with open("model.pkl", "rb") as file:
            model = pickle.load(file)
        prediction = model.predict(data)
        return prediction[0]
    except Exception as e:
        raise Exception(f"Model prediction failed: {str(e)}")


if __name__ == "__main__":
    app.run()
