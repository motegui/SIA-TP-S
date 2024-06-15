import math
import os
import random

import numpy as np

from TP3.config import config
from TP3.src.Network import Network
from TP3.src.perceptron import print_to_CSV


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
            mu = result[:len(result)/2]
            sigma = result[len(result)/2:]

            z = reparameterization_trick(mu, sigma)
            output = decoder.forward_propagation(z)
            # actualizar pesos!!!....!!!


            compute_activation = network.forward_propagation(x)
            network.back_propagation(compute_activation, exp, i)  # me modifica los delta w
            input_copy.remove(x)
            expected_copy.remove(exp)
        error = compute_error_function([input_data, expected_output], network)
        if i % 1000 == 0:
            print_to_CSV('multilayer_perceptron_errors.csv', error, i)

        if error < min_error:
            print(error)
            min_error = error
            network.update_layer_weights()

        network.reset_deltas()
        i += 1
    return min_error


def reparameterization_trick(mu, sigma):
    eps = np.random.standard_normal()
    return mu + sigma * eps
