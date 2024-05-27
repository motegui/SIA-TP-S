import numpy as np


class Neuron:
    def __init__(self, weights, x, y):
        self.weights = np.array(weights).astype(float)
        self.x = x
        self.y = y

    def update_weights(self, x, learning_rate):
        x = np.array(x).astype(float)
        self.weights += learning_rate * (x-self.weights)

    def get_weights(self):
        weights = [x.astype(float) for x in self.weights]
        return weights
