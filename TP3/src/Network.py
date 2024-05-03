from Neuron import *
from Layer import *


class Network:
    def __init__(self, layers: list[Layer]):  # Recibe las layers en orden
        self.layers = layers

    def initialize(self, input_count):
        self.layers[0].prev_layer = None
        self.layers[0].next_layer = self.layers[1]

        for i in range(1, len(self.layers) - 1):
            self.layers[i].next_layer = self.layers[i + 1]
            self.layers[i].prev_layer = self.layers[i - 1]

        self.layers[-1].prev_layer = self.layers[-2]
        self.layers[-1].next_layer = None

        # Popular los pesos de toda la red      DUDA: Se entrena siempre para la misma cantida de inputs la red? supongo que si
        self.layers[0].populate_weights(input_count)

        for layer in self.layers[1:]:
            layer.populate_weights()

    def forward_propagation(self, input_data):
        inputs = input_data
        layer = self.layers[0]
        while layer is not None:
            inputs = layer.forward(inputs)
            layer = layer.next_layer
        return inputs


def layer_n_neurons(neuron_count, theta, prime_theta):
    layer = Layer()
    neurons = []
    for i in range(neuron_count):
        neuron = Neuron(theta, prime_theta)
        neurons.append(neuron)
    layer.neurons = neurons
    return layer
