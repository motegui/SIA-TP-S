import numpy as np

from TP3.config import config
from TP3.src.utils import *


class Layer:
    def __init__(self, neurons=None):
        self.neurons = neurons
        self.neuron_len = len(neurons)

    def forward(self, inputs):
        out = []
        for neuron in self.neurons:
            neuron.set_inputs([1] + inputs)
            out.append(neuron.compute_output())
        return out

    def updated_forward(self, inputs):
        out = []
        for neuron in self.neurons:
            neuron.set_inputs([1] + inputs)
            out.append(neuron.compute_updated_output())
        return out

    def populate_weights(self, input_count=None):
        for neuron in self.neurons:
            weights = random_initialize_weight(input_count)
            neuron.set_weights(weights)  # aca hay que agregar el bias
            neuron.delta_w = np.zeros_like(neuron.weights)
            neuron.m = np.zeros_like(neuron.weights)
            neuron.v = np.zeros_like(neuron.weights)



    def get_weights(self):
        return [neuron.weights for neuron in self.neurons]

    def compute_deltas(self, prev_deltas, connected_weights, epoch):  # connected_weights es un vector de vectores y para neurona_i uso connected_i
        deltas = []
        for i in range(len(self.neurons)):
            self.neurons[i].compute_delta(prev_deltas, np.array(connected_weights)[:, i + 1])
            if config.get("optimizer") == "adam":
                self.neurons[i].adam(epoch)
            deltas.append(self.neurons[i].delta)
        return deltas

    def update_neuron_weights(self):
        for neuron in self.neurons:
            neuron.update_weights()

    def reset_deltas(self):
        for neuron in self.neurons:
            neuron.delta_w = np.zeros(len(neuron.weights))

    def __str__(self):
        return '\n'.join([str(neuron) for neuron in self.neurons])
