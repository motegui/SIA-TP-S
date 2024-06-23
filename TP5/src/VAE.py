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
    decoder.initialize(input_count=2)

    while min_error > epsilon and i < limit:
        input_copy = input_data.copy()
        expected_copy = expected_output.copy()
        for _ in range(batch_size):
            u = np.random.randint(0, len(input_copy))
            x = input_copy[u]
            exp = expected_copy[u]

            result = encoder.forward_propagation(x)
            mu = result[:len(result) // 2]
            sigma = result[len(result) // 2:]

            z, eps = reparameterization_trick(np.array(mu), np.array(sigma))
            # z = np.concatenate(([0], z))  # Añadir bias si es necesario

            output = decoder.forward_propagation(z.tolist())

            # reconstruction_loss = np.mean((output - exp) ** 2)  # Usamos MSE como ejemplo
            # kl_loss = -0.5 * np.sum(1 + np.log(sigma ** 2) - mu ** 2 - sigma ** 2)
            # total_loss = reconstruction_loss + kl_loss

            last_decoder_deltas = decoder.back_propagation(output, exp, i)

            dE_dz = last_decoder_deltas

            dE_dmu = dE_dz
            dE_dsigma = np.multiply(dE_dz, eps)  # reparam

            dE_dmu_sigma = np.concatenate((dE_dmu, dE_dsigma.tolist()))

            encoder.back_propagation2(i, dE_dmu_sigma.tolist())
        error = compute_error_VAE([input_data, input_data], network)
        if i % 1000 == 0:
            print_to_CSV('multilayer_perceptron_errors.csv', error, i)

        if error < min_error:
            min_error = error
            network.update_layer_weights()
            print(error)
        network.reset_deltas()
        i += 1
    return min_error, network


def reparameterization_trick(mu, sigma, fixed=False):
    eps = np.random.standard_normal()
    if fixed:
        eps = 1
    return mu + sigma * eps, eps


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
        mu = np.array(result[:int(len(result) / 2)])  # Convertir mu a un array de Numpy
        sigma = np.array(result[int(len(result) / 2):])  # Convertir sigma a un array de Numpy

        z, eps = reparameterization_trick(mu, sigma, fixed=True)
        # z = np.insert(z, 0, 1)

        output = decoder.forward_propagation(z.tolist())
        t = np.square(np.array(output) - np.array(expected_output[i]))

        reconstruction_error = sum(t)
        kl_error = -0.5 * np.sum(1 + np.log(sigma ** 2) - mu ** 2 - sigma ** 2)  # Calcular el error KL
        total_error = reconstruction_error + kl_error
        errors.append(total_error)
    return sum(errors) * 0.5



if __name__ == '__main__':
    # random.shuffle(letters_pattern)
    # 35 5 4 4 5 35

    layers = [
        # layer_n_neurons(            35, hyp_tan_theta, hyp_tan_prime_theta),
        layer_n_neurons(5, hyp_tan_theta, hyp_tan_prime_theta),
        layer_n_neurons(15, hyp_tan_theta, hyp_tan_prime_theta),
        layer_n_neurons(15, hyp_tan_theta, hyp_tan_prime_theta),
        layer_n_neurons(4, lineal_theta, lineal_prime_theta, is_latent=True),
        layer_n_neurons(15, hyp_tan_theta, hyp_tan_prime_theta, is_decoder=True),
        layer_n_neurons(15, hyp_tan_theta, hyp_tan_prime_theta),
        layer_n_neurons(5, hyp_tan_theta, hyp_tan_prime_theta),
        layer_n_neurons(35, hyp_tan_theta, hyp_tan_prime_theta)
    ]

    n = Network(layers)
    n.initialize(input_count=35)

    letters = get_letters()

    nor = [[-1 if elemento == 0 else elemento for elemento in fila] for fila in letters]

    error = vae(letters[:10], nor[:10], compute_error_VAE, 10000, 0, n)
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
