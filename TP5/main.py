import random
import numpy as np
from matplotlib import pyplot as plt

from TP3.src.Network import Network, layer_n_neurons, create_weighted_network
from TP3.src.Layer import Layer
from TP3.src.Neuron import Neuron
from TP3.src.perceptron import multilayer_perceptron
from TP3.src.theta_functions import hyp_tan_theta, hyp_tan_prime_theta, logistic_theta, logistic_prime_theta, \
    lineal_theta, lineal_prime_theta
from TP3.src.utils import compute_error_multilayer
from TP4.src.hopfieldUtils import find_most_orthonormal_vectors
from TP5.src.autoencoder import autoencoder, plot_latent_space
from TP5.src.utils import get_letters, test_network, get_labels_by_letters, generar_puntos_entre, cast_letter, \
    plot_letters


def pixel_error(output, expected):
    error = 0
    for i in range(len(output)):
        if output[i] > 0:
            if expected[i] != 1:
                error += 1
        else:
            if expected[i] != -1:
                error += 1
    return error


def main():
    letters_pattern = get_letters()
    # letters_pattern = find_most_orthonormal_vectors(letters_pattern, 5)[0][-1]
    print('sali de aca')
    network = autoencoder(letters_pattern, letters_pattern)
    encoder, decoder = network.get_decoder_encoder()
    plot_latent_space(letters_pattern, encoder)
    test_network(letters_pattern, letters_pattern, network)

    # voy a agarrar dos componentes del espacio latente, y me voy a ir moviendo de uno para el otro.
    l1 = letters_pattern[1]
    l2 = letters_pattern[2]

    p1 = encoder.forward_propagation(l1)
    p2 = encoder.forward_propagation(l2)

    points = generar_puntos_entre(p1, p2, 14)
    letters = [l1]
    for point in points:
        letter = decoder.forward_propagation([point[0], point[1]])
        letter = cast_letter(letter)
        letters.append(letter)
    letters.append(l2)

    plot_letters(letters)

    # Una vez qeu tenga todas esas coordenadas, voy a usar el decoder, y ver que letras me da
    # lo que me devuelva el decder lo tengo que pasar por un conversor de unos y 0's y finalmente graficarlos


if __name__ == '__main__':
    main()
