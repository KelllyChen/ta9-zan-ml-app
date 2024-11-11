# app.py
from flask import Flask, request, render_template
import joblib
import numpy as np
from sklearn.datasets import load_iris

app = Flask(__name__)

# Load the trained model and Iris dataset for target names
model = joblib.load('model.pkl')
data = load_iris()
target_names = data.target_names  # ['setosa', 'versicolor', 'virginica']

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = None
    if request.method == 'POST':
        try:
            # Extract form data and convert to floats
            sepal_length = float(request.form.get('sepal_length', 0))
            sepal_width = float(request.form.get('sepal_width', 0))
            petal_length = float(request.form.get('petal_length', 0))
            petal_width = float(request.form.get('petal_width', 0))

            # Prepare data for prediction
            input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
            predicted_class_index = model.predict(input_data)[0]  # Predict the class index

            # Get the class name from target_names using the predicted index
            prediction = target_names[predicted_class_index]

        except ValueError:
            prediction = "Error: Please enter valid numeric values."

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

