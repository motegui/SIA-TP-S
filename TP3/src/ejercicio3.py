from Neuron import *
from Layer import *
from theta_functions import *
from Network import *

def main():

    layer1 = layer_n_neurons(3, logistic_theta, logistic_prime_theta)
    layer2 = layer_n_neurons(3, logistic_theta, logistic_prime_theta)
    layer3 = layer_n_neurons(2, logistic_theta, logistic_prime_theta)
    layer4 = layer_n_neurons(5, logistic_theta, logistic_prime_theta)
    network = Network([layer1, layer2, layer3, layer4])

    network.initialize(input_count=6)

    print(network.forward_propagation([1, 2, 3, 4, 5, 6]))



if __name__ == '__main__':
    main()
