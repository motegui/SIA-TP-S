from utils import *


class Layer:
    def __init__(self, neurons, prev_layer=None, next_layer=None):
        self.neurons = neurons
        self.prev_layer = prev_layer
        self.next_layer = next_layer

    def forward(self, inputs):
        out = []
        for neuron in self.neurons:
            neuron.set_inputs(inputs)
            out.append(neuron.compute_excitement())
        return out

    def populate_weights(self):
        for neuron in self.neurons:
            weights = random_initialize_weight(len(self.prev_layer.neurons))
            neuron.set_weights(weights)  # aca hay que agregar el bias?
