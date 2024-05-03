from Neuron import *
from Layer import *
from theta_functions import *


def main():
    neuron4 = Neuron(theta=logistic_theta, prime_theta=logistic_prime_theta)
    neuron5 = Neuron(theta=logistic_theta, prime_theta=logistic_prime_theta)
    layer1 = Layer([neuron4, neuron5])

    neuron6 = Neuron(theta=logistic_theta, prime_theta=logistic_prime_theta)
    neuron7 = Neuron(theta=logistic_theta, prime_theta=logistic_prime_theta)
    neuron8 = Neuron(theta=logistic_theta, prime_theta=logistic_prime_theta)
    layer2 = Layer([neuron6, neuron7, neuron8])

    layer1.next_layer = layer2
    layer1.prev_layer = None
    layer2.prev_layer = layer1

    input_values = [1, 2, 3]

    layer1.populate_weights(input_values)   # NOTA: la primera layer se inicializa con el input para saber cuantos
                                            # pesos va a tener.(seria la capa 0 pero me parece que no hace nada esa
                                            #capa mas que mandar el input a la capa 1.)
    layer2.populate_weights()

    forward_propagation(layer1, input_values)
    print("hola")


if __name__ == '__main__':
    main()
