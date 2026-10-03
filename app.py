from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained KNN model and preprocessor
knn_model = joblib.load("knn_model.pkl")
preprocessor = joblib.load("preprocessor.pkl")


# Home page
@app.route("/")
def home():
    return render_template("index.html")


# Prediction API
@app.route("/predict", methods=["POST"])
def predict():

    data = request.json

    input_data = pd.DataFrame([data])

    # Apply the same preprocessing used during model training
    processed_data = preprocessor.transform(input_data)

    # Make prediction
    prediction = knn_model.predict(processed_data)[0]

    if prediction:
        result = "Purchase"
    else:
        result = "No Purchase"

    return jsonify({
        "prediction": result
    })


if __name__ == "__main__":
    app.run(debug=True)