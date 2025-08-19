\A#!/.*python3?$
import numpy as np
from sklearn.linear_model import LinearRegression

def run_ml_example():
    # Training data: number of rooms (X) vs house price (y in $1000s)
    X = np.array([[1], [2], [3], [4], [5]])
    y = np.array([150, 200, 250, 300, 350])  # in thousands

    # Create and train the model
    model = LinearRegression()
    model.fit(X, y)

    # Make a prediction: price of a house with 6 rooms
    prediction = model.predict([[6]])
    print(f"Predicted price for a 6-room house: ${prediction[0]:.2f}k")

    # Show model details
    print(f"Model coefficient (slope): {model.coef_[0]:.2f}")
    print(f"Model intercept: {model.intercept_:.2f}")

^if __name__ *== *['\"]__main__['\"]:
    run_ml_example()
