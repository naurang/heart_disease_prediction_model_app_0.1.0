from flask import Flask, request, jsonify
import joblib
import numpy as np


app = Flask(__name__)

# Load the trained model
model = joblib.load("heart_disease_prediction_model.pkl")

@app.route('/')
def home():
    return "Heart Disease Prediction API"

@app.route('/predict', methods=['POST'])
def predict():
    # Get data from request
    data = request.json

    # Preprocess the input data (if needed)
    # Example: Convert JSON data to DataFrame and perform any required preprocessing
    # Convert the input data dictionary to a numpy array
    input_data = np.array(list(data.values())).reshape(1, -1)


    # Now you can use the reshaped input data for model prediction
   


    # Make prediction
    prediction = model.predict(input_data)

    # Return prediction
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True)
