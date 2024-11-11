import joblib
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier

# Load data and train a simple model
data = load_iris()
X, y = data.data, data.target
model = KNeighborsClassifier()
model.fit(X, y)

# Save the model
joblib.dump(model, 'model.pkl')

