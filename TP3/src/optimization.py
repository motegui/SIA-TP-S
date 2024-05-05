import numpy as np


def gradient_descend(step, neuron):
    t = np.multiply(step * neuron.delta, neuron.inputs).tolist()
    return t


