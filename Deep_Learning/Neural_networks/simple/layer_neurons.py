import numpy as np

# Inputs 
inputs = [1, 3, 5, 7]

# Weights 
weights1 = [0.1, 0.2, 0.3, -0.1]
weights2 = [0.4, 0.5, 0.6, -0.2]
weights3 = [0.7, 0.8, 0.9, -0.3]

# Bias
bias1 = 1
bias2 = 2
bias3 = 3

# Outputs
outputs = [

    # Neurons 1
    inputs[0] * weights1[0] +
    inputs[1] * weights1[1] +
    inputs[2] * weights1[2] +
    inputs[3] * weights1[3] +
    bias1,

    # Neurons 2
    inputs[0] * weights2[0] +
    inputs[1] * weights2[1] +
    inputs[2] * weights2[2] +
    inputs[3] * weights2[3] +
    bias2,

    # Neurons 3
    inputs[0] * weights3[0] +
    inputs[1] * weights3[1] +
    inputs[2] * weights3[2] +
    inputs[3] * weights3[3] +
    bias3
]

print(f"Layer of 3 neurons :-: {outputs}")
