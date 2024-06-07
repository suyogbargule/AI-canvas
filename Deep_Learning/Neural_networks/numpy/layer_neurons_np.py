import numpy as np

# Input 5 node
inputs  = [1, 2, 3, 4, 5]

# Weights 3X5 
weights = [[ 0.1, 0.2,  0.3,  0.4,  -0.1],
           [ 0.5, 0.6,  0.7,  0.8,  -0.2],
           [ 0.9, 0.10, 0.11, 0.12, -0.3]]

# Biases
biases =  [1, 2, 3]

# Output
output = np.dot (weights, inputs) + biases

print(f"Layer of {len(inputs)} neurons :-: {output}")