import math
import os
import random

import numpy as np

from TP3.config import config
from TP3.src.Network import Network, layer_n_neurons
from TP3.src.perceptron import print_to_CSV
from TP3.src.theta_functions import lineal_theta, hyp_tan_theta, hyp_tan_prime_theta, lineal_prime_theta
from TP3.src.utils import compute_error_multilayer
from TP5.src.autoencoder import plot_latent_space
from TP5.src.utils import get_letters, test_network, plot_progress


def vae(input_data, expected_output, compute_error_function, limit, epsilon, network: Network):
    if limit == 0:
        limit = math.inf
    i = 0
    min_error = math.inf
    batch_size = config.get('batch_size')
    csv_path = 'multilayer_perceptron_errors.csv'
    # Eliminar el archivo si existe antes de comenzar las iteraciones
    if os.path.exists(csv_path):
        os.remove(csv_path)
    encoder, decoder = network.get_decoder_encoder()

    while min_error > epsilon and i < limit:
        input_copy = input_data.copy()
        expected_copy = expected_output.copy()
        for _ in range(batch_size):
            u = random.randint(0, len(input_copy) - 1)
            x = input_copy[u]
            exp = expected_copy[u]
            result = encoder.forward_propagation(x)
            mu = result[:int(len(result) / 2)]
            sigma = result[int(len(result) / 2):]

            z, eps = reparameterization_trick(mu, sigma)
            output = decoder.forward_propagation(z)
            last_decoder_deltas = decoder.back_propagation(output, exp, i)

            dE_dmu = last_decoder_deltas
            dE_dsigma = eps * np.array(last_decoder_deltas)
            error = np.concatenate((dE_dmu, dE_dsigma))
            encoder.back_propagation(np.zeros(len(error)), error, i)

            dL_dm = mu
            dL_dv = 0.5 * (np.exp(sigma) - 1)
            error = np.concatenate((dL_dm, dL_dv))
            encoder.back_propagation(np.zeros(len(error)), error, i)
            # compute_activation = network.forward_propagation(x)
            # network.back_propagation(compute_activation, exp, i)  # me modifica los delta w
            input_copy.remove(x)
            expected_copy.remove(exp)
        error = get_reconstruction_error(output, exp, mu, sigma)
        if i % 1000 == 0:
            print_to_CSV('multilayer_perceptron_errors.csv', error, i)

        if error < min_error:
            print(error)
            min_error = error
            network.update_layer_weights()

        network.reset_deltas()
        i += 1
    return min_error,network


def reparameterization_trick(mu, sigma):
    eps = np.random.standard_normal()
    return np.array(mu) + np.array(sigma) * eps, eps


def get_reconstruction_error(output_data, expected_output, mu, sigma):
    output_data = np.array(output_data)
    expected_output = np.array(expected_output)
    mu = np.array(mu)
    sigma = np.array(sigma)
    rec = 0.5 * np.mean((expected_output - output_data) ** 2)
    kl = -0.5 * np.sum(1 + sigma - mu ** 2 - np.exp(sigma))
    return rec + kl


if __name__ == '__main__':
    # random.shuffle(letters_pattern)
    layer1 = layer_n_neurons(25, lineal_theta, lineal_prime_theta)
    layer2 = layer_n_neurons(25, lineal_theta, lineal_prime_theta)
    layer5 = layer_n_neurons(2, lineal_theta, lineal_prime_theta, is_latent=True)
    layer8 = layer_n_neurons(25, hyp_tan_theta, hyp_tan_prime_theta)
    layer9 = layer_n_neurons(25, hyp_tan_theta, hyp_tan_prime_theta)
    layer10 = layer_n_neurons(35, hyp_tan_theta, hyp_tan_prime_theta)

    n = Network([layer1, layer5, layer8, layer10])
    n.initialize(input_count=35)

    letters = get_letters()
    error = vae(letters, letters, compute_error_multilayer, 10000, 0, n)
    print(error)

    encoder, decoder = n.get_decoder_encoder()

    plot_latent_space(letters, letters, encoder)
    test_network(letters, letters, n)

    # voy a agarrar dos componentes del espacio latente, y me voy a ir moviendo de uno para el otro.

    l1 = letters[1]
    l2 = letters[2]

    plot_progress(l1, l2, encoder, decoder)

    l1 = letters[3]
    l2 = letters[10]
    plot_progress(l1, l2, encoder, decoder)
