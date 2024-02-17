# heart_disease_prediction_model_app_0.1.0
---

# Heart Disease Prediction Web Application

This project is a Flask web application that predicts the likelihood of heart disease based on various medical attributes provided by the user. It utilizes a machine learning model trained on the Cleveland Heart Disease dataset.

## Project Overview

The project consists of the following components:

1. **Flask Web Application**: Provides a user interface for inputting medical attributes and obtaining predictions.
2. **Machine Learning Model**: Utilizes logistic regression to predict the presence of heart disease.
3. **Data Processing**: Preprocesses the input data and prepares it for prediction by the model.

## Requirements

To run the project locally, you need the following software installed on your machine:

- Python (version 3.x)
- Flask
- scikit-learn
- pandas
- numpy

You can install these dependencies using pip:

```bash
pip install flask scikit-learn pandas numpy
```

## Running the Application

To run the Flask web application, execute the following command in your terminal:

```bash
python app.py
```

This will start the Flask development server, and you can access the web application by navigating to `http://127.0.0.1:5000` in your web browser.

## Usage

Once the application is running, you can input medical attributes related to heart disease (e.g., age, sex, cholesterol level) into the provided form. After submitting the form, the application will display the predicted likelihood of heart disease.

## References

- Cleveland Heart Disease dataset: [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Heart+Disease)
- Flask documentation: [Flask Website](https://flask.palletsprojects.com/)
- scikit-learn documentation: [scikit-learn Website](https://scikit-learn.org/stable/)

## Author

Suraj Singh

---
