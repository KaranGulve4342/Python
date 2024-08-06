import numpy as np

class LinearRegression:

    def __init__(self, lr=0.01, n_iters=1000):
        self.lr = lr  # Learning rate
        self.n_iters = n_iters  # Number of iterations
        self.weights = None  # Weights (to be learned)
        self.bias = None  # Bias (to be learned)

    def fit(self, X, y):
        n_samples, n_features = X.shape  # Number of samples and features
        self.weights = np.zeros(n_features)  # Initialize weights to zeros
        self.bias = 0  # Initialize bias to zero

        for _ in range(self.n_iters):
            y_pred = np.dot(X, self.weights) + self.bias  # Predicted values

            # Compute gradients
            dw = (1 / n_samples) * np.dot(X.T, (y_pred - y))  # Gradient of weights
            db = (1 / n_samples) * np.sum(y_pred - y)  # Gradient of bias

            # Update weights and bias
            self.weights -= self.lr * dw
            self.bias -= self.lr * db

    def predict(self, X):
        y_pred = np.dot(X, self.weights) + self.bias  # Compute predicted values
        return y_pred