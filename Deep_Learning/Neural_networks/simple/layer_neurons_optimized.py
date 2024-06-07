import numpy as np 

# Inputs 
inputs = [1, 3, 5, 7]

# Weights 
weights  = [ [0.1,  0.2,  0.3,  -0.1],
             [0.4,  0.5,  0.6,  -0.2],
             [0.7,  0.8,  0.9,  -0.3],
             [0.10, 0.11, 0.12, -0.4] ]

# Bias
biases = [1, 2, 3, 4]

# Output of current layer
layer_outputs  = []

# For each neuron
for neuron_weights, neuron_bias in zip(weights, biases):
    
    # Zeroed output of given neuron
    neuron_output = 0
    
    # For each input and weight to the neuron
    for n_input, weight in zip(inputs, neuron_weights):
        
        # Multiply this input by associated weight
        # and add to the neuron’s output variable
        neuron_output += n_input * weight

    # Add bias
    neuron_output += neuron_bias

    # Put neuron’s result to the layer’s output list
    layer_outputs.append(neuron_output)

print(layer_outputs)