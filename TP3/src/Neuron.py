import numpy as np


class Neuron:

    def __init__(self, theta, prime_theta, weights):
        self.delta = None
        self.theta = theta
        self.prime_theta = prime_theta
        self.weights = weights
        self.inputs = []

    def compute_excitement(self):
        if self.inputs is None:
            return None
        return sum(np.multiply(self.inputs, self.weights))

    def set_inputs(self, inputs):
        self.inputs = [1] + inputs

    def set_delta(self, delta):
        self.delta = delta

    def set_weights(self, weights):
        self.weights = weights

    