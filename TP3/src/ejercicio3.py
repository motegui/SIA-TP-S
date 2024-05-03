from Neuron import *
from Layer import *
from theta_functions import *
from Network import *
from perceptron import multilayer_perceptron


def main():
    layer1 = layer_n_neurons(2, hyp_tan_theta, hyp_tan_prime_theta)
    layer2 = layer_n_neurons(1, hyp_tan_theta, hyp_tan_prime_theta)
    layer3 = layer_n_neurons(4, hyp_tan_theta, hyp_tan_prime_theta)
    layer4 = layer_n_neurons(3, hyp_tan_theta, hyp_tan_prime_theta)
    network = Network([layer1, layer2])

    network.initialize(input_count=2)
    input_data = [[1, 1], [1, -1], [-1, 1], [-1, -1]]
    output_data = [[-1], [1], [1], [-1]]
    error = multilayer_perceptron(input_data, output_data, compute_error_multilayer, 200000, 0, network)

    print(error)

    print(network.forward_propagation([1, 1]))
    print(network.forward_propagation([1, -1]))

    print(network)


if __name__ == '__main__':
    main()
