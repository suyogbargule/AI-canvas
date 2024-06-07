import numpy as np

inputs = [1, 2, 3, 4, 5]
weights = [0.1, 0.2, 0.3, 0.4, 0.5]
bias = 1

output = np.dot(weights, inputs) + bias

print(f"Single neuron output :-: {output}")