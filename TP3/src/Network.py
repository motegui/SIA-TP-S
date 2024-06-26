import numpy as np

from TP3.src.Layer import *
from TP3.config import config
from TP3.src.Neuron import Neuron
from TP3.src.optimization import gradient_descend
from TP3.src.theta_functions import hyp_tan_theta, hyp_tan_prime_theta


class Network:
    def __init__(self, layers: list[Layer]):  # Recibe las layers en orden
        self.layers = layers

    def initialize(self, input_count):
        self.layers[0].populate_weights(input_count)

        for i in range(1, len(self.layers)):
            self.layers[i].populate_weights(self.layers[i - 1].neuron_len)

    def forward_propagation(self, input_data):
        inputs = input_data
        i = 0
        last_layer_latent = False
        for layer in self.layers:
            i += 1
            # print(inputs, i)
            if layer.is_decoder and last_layer_latent:
                z, _ = reparameterization_trick(inputs[:len(inputs) // 2], inputs[len(inputs) // 2:])
                inputs = layer.forward(z.tolist())
                last_layer_latent = False
            else:
                inputs = layer.forward(inputs)

            if layer.is_latent:
                last_layer_latent = True
        return inputs

    def updated_forward_propagation(self, input_data):
        inputs = input_data
        for layer in self.layers:
            inputs = layer.updated_forward(inputs)
        return inputs

    def fix_weights(self):
        self.layers[0].fix_weights()

    def back_propagation(self, forward_output, expected_output, epoch):
        prev_deltas = []
        for i in range(len(self.layers) - 1, -1, -1):
            layer = self.layers[i]
            if i == len(self.layers) - 1:
                #  calcular deltas de la primera capa. -> funcion distinta
                for j in range(len(layer.neurons)):
                    t = layer.neurons[j].compute_excitement()
                    op = expected_output[j] - forward_output[j]
                    layer.neurons[j].delta = np.multiply(op, layer.neurons[j].prime_theta(t))
                    layer.neurons[j].delta_w += gradient_descend(config.get("step"), layer.neurons[j])
                    if config.get("optimizer") == "adam":
                        layer.neurons[j].adam(epoch)

                    if config.get("optimizer") == "momentum":
                        layer.neurons[j].momentum_optimizer(epoch)

                    prev_deltas.append(layer.neurons[j].delta)
            else:
                # calcular delta -> funcion norma
                connected_weights = self.layers[i + 1].get_weights()
                prev_deltas = layer.compute_deltas(prev_deltas, connected_weights, epoch)
        return prev_deltas

    def back_propagation2(self, epoch, grad):
        prev_deltas = grad  # Start with the given gradients
        for i in range(len(self.layers) - 1, -1, -1):
            layer = self.layers[i]
            if i == len(self.layers) - 1:

                # ACA HAY QUE FIXEAR CREO. hay que hacer el enganche como para que siga la backprop.
                # Tiene que ser casi igual al else (porque no hay que hacer lo de calcular de nuevo los deltas)
                # pero me da dudas el tema de usar connected_weights como todos 1.

                connected_weights = np.ones((len(prev_deltas), len(layer.neurons) + 1))
                prev_deltas = layer.compute_deltas(prev_deltas, connected_weights, epoch)
            else:
                # For other layers, calculate delta normally
                connected_weights = self.layers[i + 1].get_weights()
                prev_deltas = layer.compute_deltas(prev_deltas, connected_weights, epoch)
        return prev_deltas

    def get_weights(self):
        weights = []
        for layer in self.layers:
            layer_weights = []
            for neuron in layer.neurons:
                if isinstance(neuron.weights, np.ndarray):
                    neuron_weights = neuron.weights.tolist()
                else:
                    neuron_weights = neuron.weights
                layer_weights.append(neuron_weights)
            weights.append(layer_weights)
        return weights

    def __str__(self):
        return '\n'.join([str(t) for t in self.layers])

    def update_layer_weights(self):
        for layer in self.layers:
            layer.update_neuron_weights()

    def reset_deltas(self):
        for layer in self.layers:
            layer.reset_deltas()

    def get_decoder_encoder(self):
        for i in range(0, len(self.layers)):
            if self.layers[i].is_latent:
                encoder = Network(self.layers[:i + 1])
                decoder = Network(self.layers[i + 1:])
                # decoder.fix_weights()
                return encoder, decoder


def layer_n_neurons(neuron_count, theta, prime_theta, is_latent=False, is_decoder=False):
    neurons = []
    for i in range(neuron_count):
        neuron = Neuron(theta, prime_theta)
        neurons.append(neuron)
    return Layer(neurons, is_latent, is_decoder)


def create_weighted_network(weights, theta, prime_theta):
    layers = []
    for layer in weights:
        if len(layer) == 2:
            theta = hyp_tan_theta
            prime_theta = hyp_tan_prime_theta

        neurons = []
        for neuron_weights in layer:
            neurons.append(Neuron(weights=neuron_weights, theta=theta, prime_theta=prime_theta))
        lay = Layer(neurons, len(neurons) == 2)
        lay.reset_deltas()
        layers.append(lay)
    return Network(layers)

def reparameterization_trick(mu, sigma, fixed=False):
    eps = np.random.standard_normal()
    if fixed:
        eps = 1
    return np.array(mu) + np.array(sigma) * eps, eps