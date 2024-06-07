import numpy as np

# Inputs 
inputs = [1, 3, 5]

# Weights
weights = [0.1, 0.2, 0.3]

# Bias
bias = 1

# Calculate outputs
output = (inputs[0] * weights[0] +
           inputs[1] * weights[1] + 
           inputs[2] * weights[2] +
           bias)

print(f"Single neuron output :-: {output}")
