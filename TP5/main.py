import numpy as np

from TP3.src.Network import Network, layer_n_neurons
from TP3.src.Layer import Layer
from TP3.src.Neuron import Neuron
from TP3.src.perceptron import multilayer_perceptron
from TP3.src.theta_functions import hyp_tan_theta, hyp_tan_prime_theta
from TP3.src.utils import compute_error_multilayer


def main():
    layer2 = layer_n_neurons(3, hyp_tan_theta, hyp_tan_prime_theta)
    layer3 = layer_n_neurons(2, hyp_tan_theta, hyp_tan_prime_theta)
    layer4 = layer_n_neurons(3, hyp_tan_theta, hyp_tan_prime_theta)
    layer5 = layer_n_neurons(5, hyp_tan_theta, hyp_tan_prime_theta)
    network = Network([layer2, layer3, layer4, layer5])

    network.initialize(input_count=5)

    input_data = [[1, 1, 1, 1, 1], [0, 0, 0, 0, 0], [1, 0, 1, 0, 1], [1, 2, 3, 4, 5]]

    error = multilayer_perceptron(input_data, input_data, compute_error_multilayer, 10000, 0.1, network)
    print(network.forward_propagation(input_data[2]))


if __name__ == '__main__':
    main()
