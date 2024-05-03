from utils import *


class Layer:
    def __init__(self, neurons=None, prev_layer=None, next_layer=None):
        self.neurons = neurons
        self.prev_layer = prev_layer
        self.next_layer = next_layer

    def forward(self, inputs):
        out = []
        for neuron in self.neurons:
            neuron.set_inputs(inputs)
            out.append(neuron.compute_output())
        return out

    def populate_weights(self, input_count=None):
        for neuron in self.neurons:
            if self.prev_layer is None:
                weights = random_initialize_weight(input_count-1)
            else:
                weights = random_initialize_weight(len(self.prev_layer.neurons)-1)
            neuron.set_weights([0] + weights)  # aca hay que agregar el bias?
