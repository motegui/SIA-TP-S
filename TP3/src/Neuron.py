import numpy as np
from optimization import *
from TP3.config import *


class Neuron:

    def __init__(self, theta, prime_theta, weights=None):
        self.delta = None
        self.delta_w = None
        self.theta = theta
        self.prime_theta = prime_theta
        self.weights = weights
        self.inputs = []

    def compute_output(self):
        t = np.multiply(self.inputs, self.weights)
        return self.theta(sum(t))

    def compute_updated_output(self):
        return self.theta(sum(np.multiply(self.inputs, np.array(self.weights) + np.array(self.delta_w))))

    def compute_excitement(self):
        t = np.multiply(self.inputs, self.weights)
        return sum(t)

    def set_inputs(self, inputs):
        self.inputs = inputs

    def set_delta(self, delta):
        self.delta = delta

    def set_weights(self, weights):
        self.weights = weights

    def compute_delta(self, prev_deltas, connected_weights):
        self.delta = sum(np.multiply(prev_deltas, connected_weights)) * self.prime_theta(self.compute_excitement())
        self.delta_w = optimizers.get(config.get("optimizer"))(config.get("step"), self)
        return self.delta

    def update_weights(self):
        self.weights = np.array(self.weights) + np.array(self.delta_w)

    def __str__(self):
        # return str(str(self.weights), str(self.inputs), str(self.delta))
        return f"weights: {self.weights}, inputs: {self.inputs} DELTA: {self.delta}"
