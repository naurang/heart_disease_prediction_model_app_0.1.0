import requests

# Sample input data for prediction
input_data = {
    'age': 63,
    'sex': 1,
    'cp': 3,
    'trestbps': 145,
    'chol': 233,
    'fbs': 1,
    'restecg': 0,
    'thalach': 150,
    'exang': 0,
    'oldpeak': 2.3,
    'slope': 0,
    'ca': 0,
    'thal': 1
}

# Make a POST request to the Flask application
response = requests.post('http://127.0.0.1:5000/predict', json=input_data)

# Print the prediction result
print(response.json())
