import numpy as np
import matplotlib.pyplot as plt
# Generate some data
def data(quantity, dimension):
    data = [np.random.rand(dimension) for _ in range(quantity)]
    return np.array(data)
def print_data(data):
    print(f"Random data has {len(data)} data points:")
    for i in range(len(data)):
        print(f"Data point {i}: {data[i]}")
data = data(10, 2)
print_data(data)
# Plot the data
def plot_data(data):
    plt.scatter(data[:, 0], data[:, 1])
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Random Data")
    plt.show()
plot_data(data)
# Fit a line to the data
def fit_line(data):
    x = data[:, 0]
    y = data[:, 1]
    A = np.vstack([x, np.ones(len(x))]).T
    m, c = np.linalg.lstsq(A, y, rcond=None)[0]
    return m, c
m, c = fit_line(data)
print(f"The line of best fit is y = {m}x + {c}")
# Plot the data and the line
def plot_line(data, m, c):
    plt.scatter(data[:, 0], data[:, 1])
    plt.plot(data[:, 0], m * data[:, 0] + c, color="red")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Random Data and Line of Best Fit")
    plt.show()
plot_line(data, m, c)