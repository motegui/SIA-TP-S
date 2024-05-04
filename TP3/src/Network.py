import numpy as np

from Neuron import *
from Layer import *


class Network:
    def __init__(self, layers: list[Layer]):  # Recibe las layers en orden
        self.layers = layers

    def initialize(self, input_count):
        self.layers[0].populate_weights(input_count)

        for i in range(1, len(self.layers)):
            self.layers[i].populate_weights(self.layers[i - 1].neuron_len)

    def forward_propagation(self, input_data):
        inputs = input_data
        for layer in self.layers:
            inputs = layer.forward(inputs)
        return inputs

    def updated_forward_propagation(self, input_data):
        inputs = input_data
        for layer in self.layers:
            inputs = layer.updated_forward(inputs)
        return inputs

    def back_propagation(self, forward_output, expected_output):
        prev_deltas = []
        for i in range(len(self.layers) - 1, -1, -1):
            layer = self.layers[i]
            if i == len(self.layers) - 1:
                #  calcular deltas de la primera capa. -> funcion distinta
                for j in range(len(layer.neurons)):
                    t = layer.neurons[j].compute_excitement()
                    op = expected_output[j] - forward_output[j]
                    layer.neurons[j].delta = np.multiply(op, layer.neurons[j].prime_theta(t))
                    layer.neurons[j].delta_w = gradient_descend(config.get("step"), layer.neurons[j].delta,
                                                                layer.neurons[j].inputs)
                    prev_deltas.append(layer.neurons[j].delta)
            else:
                # calcular delta -> funcion norma
                connected_weights = self.layers[i + 1].get_weights()
                prev_deltas = layer.compute_deltas(prev_deltas, connected_weights)

    def __str__(self):
        return '\n'.join([str(t) for t in self.layers])

    def update_layer_weights(self):
        for layer in self.layers:
            layer.update_neuron_weights()


def layer_n_neurons(neuron_count, theta, prime_theta):
    neurons = []
    for i in range(neuron_count):
        neuron = Neuron(theta, prime_theta)
        neurons.append(neuron)
    return Layer(neurons)
