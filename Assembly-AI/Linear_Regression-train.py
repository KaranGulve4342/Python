import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets
import matplotlib.pyplot as plt
from Linear_Regression import LinearRegression

# Generate dataset
X, y = datasets.make_regression(n_samples=100, n_features=1, noise=20, random_state=4)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)

# Plot the dataset
fig = plt.figure(figsize=(8, 6))
plt.scatter(X[:, 0], y, color='b', marker='o', s=30)
# plt.show()

# Instantiate the LinearRegression object
regressor = LinearRegression()

# Fit the model
regressor.fit(X_train, y_train)

# Make predictions
predictions = regressor.predict(X_test)

# Debugging: Print y_test and predictions
print("y_test:", y_test)
print("predictions:", predictions)

# Define mean squared error function
def mean_squared_error(y_test, predictions):
    return np.mean((y_test - predictions)**2)

# Calculate mean squared error
mse = mean_squared_error(y_test, predictions)
print("Mean Squared Error:", mse)

# Plot the predictions
y_pred_line = regressor.predict(X)
cmap = plt.get_cmap('viridis')
fig = plt.figure(figsize=(8, 6))
m1 = plt.scatter(X_train, y_train, color=cmap(0.9), s=10)
m2 = plt.scatter(X_test, y_test, color=cmap(0.5), s=10)
plt.plot(X, y_pred_line, color='black', linewidth=2, label='Prediction')
plt.show()