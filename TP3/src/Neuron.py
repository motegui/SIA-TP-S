import numpy as np
from TP3.config import *


class Neuron:

    def __init__(self, theta, prime_theta, weights=None):
        self.delta = None
        self.delta_w = None
        self.theta = theta
        self.prime_theta = prime_theta
        self.weights = weights
        self.inputs = []
        # adam parameters
        self.m = None
        self.v = None
        # momentum_parameters
        self.momentum = None
        # momentum_parameters
        self.momentum = None
        self.delta_w = None

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
        self.momentum = np.zeros_like(weights)  # Initialize momentum with the same shape as weights

    def compute_delta(self, prev_deltas, connected_weights):
        self.delta = sum(np.multiply(prev_deltas, connected_weights)) * self.prime_theta(self.compute_excitement())
        self.delta_w += gradient_descend(config.get("step"), self)
        return self.delta

    def update_weights(self):
        self.weights = np.array(self.weights) + np.array(self.delta_w)

    def adam(self, epoch):
        self.m = (config.get("b1") * self.m + (1 - config.get("b1")) * (self.delta_w))
        self.v = (config.get("b2") * self.v + (1 - config.get("b2")) * (self.delta_w) ** 2)
        m_hat = self.m / (1 - config.get("b1") ** (epoch + 1))
        v_hat = self.v / (1 - config.get("b2") ** (epoch + 1))
        self.delta_w = config.get("step") * m_hat / (np.sqrt(v_hat) + config.get("e"))

    def momentum_optimizer(self, epoch):
        self.momentum = config.get("momentum") * self.momentum + self.delta_w
        self.delta_w -= self.momentum

    def __str__(self):
        # return str(str(self.weights), str(self.inputs), str(self.delta))
        return f"weights: {self.weights}, inputs: {self.inputs} DELTA: {self.delta}"
