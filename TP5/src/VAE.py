import math
import os
import random

import numpy as np

from TP3.config import config
from TP3.src.Network import Network, layer_n_neurons
from TP3.src.perceptron import print_to_CSV
from TP3.src.theta_functions import lineal_theta, hyp_tan_theta, hyp_tan_prime_theta, lineal_prime_theta, \
    logistic_theta, logistic_prime_theta
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

            z, eps = reparameterization_trick(mu, sigma) # z tiene (a, b)

            z = np.concatenate(([1], z))
            output = decoder.forward_propagation(z)

            last_decoder_deltas = decoder.back_propagation(output, exp, i)

            dE_dmu = last_decoder_deltas[:4]
            dE_dsigma = eps * np.array(last_decoder_deltas[:4])

            gradients = np.concatenate((dE_dmu, dE_dsigma))
            encoder.back_propagation2(np.zeros(len(gradients)), gradients, i, gradients)

            dL_dm = np.multiply(mu, -1)
            dL_dv = -0.5 * (np.exp(sigma) - 1)
            error = np.concatenate((dL_dm, dL_dv))
            # compute_activation = network.forward_propagation(x)
            # network.back_propagation(compute_activation, exp, i)  # me modifica los delta w
            input_copy.remove(x)
            expected_copy.remove(exp)
        error = compute_error_VAE([input_data, input_data], network)
        if i % 1000 == 0:
            print_to_CSV('multilayer_perceptron_errors.csv', error, i)
        print(error)

        # if error < min_error:
        # min_error = error
        network.update_layer_weights()

        network.reset_deltas()
        i += 1
    return min_error, network


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

def compute_error_VAE(data, network):
    input_data = data[0]
    expected_output = data[1]
    errors = []
    encoder, decoder = network.get_decoder_encoder()
    for i in range(len(input_data)):
        result = encoder.forward_propagation(input_data[i])
        mu = result[:int(len(result) / 2)]
        sigma = result[int(len(result) / 2):]

        z, eps = reparameterization_trick(mu, sigma)
        z = np.insert(z, 0, 1)

        output = decoder.forward_propagation(z)
        t = np.square(np.array(output) - np.array(expected_output[i]))

        errors.append(sum(t))
    return sum(errors) * 0.5


if __name__ == '__main__':
    # random.shuffle(letters_pattern)
    layer1 = layer_n_neurons(5, hyp_tan_theta, hyp_tan_prime_theta)
    layer22 = layer_n_neurons(25, lineal_theta, lineal_prime_theta)
    layer23 = layer_n_neurons(25, lineal_theta, lineal_prime_theta)
    layer24 = layer_n_neurons(25, lineal_theta, lineal_prime_theta)
    layer25 = layer_n_neurons(25, lineal_theta, lineal_prime_theta)
    layer26 = layer_n_neurons(5, hyp_tan_theta, hyp_tan_prime_theta)
    layer2 = layer_n_neurons(25, lineal_theta, lineal_prime_theta)
    layer3 = layer_n_neurons(25, lineal_theta, lineal_prime_theta)
    layer4 = layer_n_neurons(25, hyp_tan_theta, hyp_tan_prime_theta)
    layer5 = layer_n_neurons(4, lineal_theta, lineal_prime_theta, is_latent=True)
    layer6 = layer_n_neurons(25, lineal_theta, lineal_prime_theta)
    layer7 = layer_n_neurons(35, hyp_tan_theta, hyp_tan_prime_theta)
    layer8 = layer_n_neurons(25, hyp_tan_theta, hyp_tan_prime_theta, is_decoder=True)
    layer9 = layer_n_neurons(5, hyp_tan_theta, hyp_tan_prime_theta)
    layer10 = layer_n_neurons(5, hyp_tan_theta, hyp_tan_prime_theta)
    layer11 = layer_n_neurons(35, hyp_tan_theta, hyp_tan_prime_theta)
    layer12 = layer_n_neurons(35, hyp_tan_theta, hyp_tan_prime_theta)
    layer13 = layer_n_neurons(35, hyp_tan_theta, hyp_tan_prime_theta)
    layer14 = layer_n_neurons(35, hyp_tan_theta, hyp_tan_prime_theta)
    layer15 = layer_n_neurons(35, hyp_tan_theta, hyp_tan_prime_theta)

    n = Network(
        [layer1, layer26, layer2, layer5, layer8, layer9, layer10, layer15])
    n.initialize(input_count=35)

    letters = get_letters()

    nor = [[-1 if elemento == 0 else elemento for elemento in fila] for fila in letters]

    error = vae(letters[:10], nor[:10], compute_error_VAE, 100000, 0, n)
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
