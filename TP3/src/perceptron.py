import math
import random
import numpy as np
from TP3.config import config
import csv


def staggered_perceptron(input_data, expected_output, initialize_weight, compute_error_function, limit, step, theta):
    i = 0

    w = initialize_weight(len(input_data[0]))
    min_error = math.inf
    w_min = None
    while min_error > 0 and i < limit:
        u = random.randint(0, len(input_data) - 1)  # u es mu
        x = [1] + input_data[u]
        h = sum(np.multiply(x, w))  # compute
        o = 1 if h >= 0 else -1  # compute activation
        delta_w = np.multiply(step * (expected_output[u] - o), x)
        w += delta_w
        error = compute_error_function([input_data, expected_output], w, theta)
        if error < min_error:
            min_error = error
            w_min = w.copy()
        i += 1
    return w_min, min_error


def lineal_nonlineal_perceptron(input_data, expected_output, initialize_weight, compute_error_function, limit, step,
                                epsilon, theta, theta_prime):
    i = 0
    w = initialize_weight(len(input_data[0]))
    min_error = math.inf
    w_min = None
    while min_error > epsilon and i < limit:
        u = random.randint(0, len(input_data) - 1)  # u es mu
        x = [1] + input_data[u]
        h = sum(np.multiply(x, w))  # compute
        o = theta(h)  # compute activation
        delta_w = np.multiply(step * (expected_output[u] - o) * theta_prime(h), x)
        w += delta_w
        error = compute_error_function([input_data, expected_output], w, theta)
        if error < min_error:
            min_error = error
            w_min = w.copy()
        i += 1
    return w_min, min_error


def multilayer_perceptron(input_data, expected_output, compute_error_function, limit, epsilon, network):
    if limit == 0:
        limit = math.inf
    i = 0
    min_error = math.inf
    batch_size = config.get('batch_size')
    while min_error > epsilon and i < limit:
        input_copy = input_data.copy()
        for _ in range(batch_size):
            u = random.randint(0, len(input_copy) - 1)
            x = input_copy[u]
            compute_activation = network.forward_propagation(x)
            network.back_propagation(compute_activation, expected_output[u])  # me modifica los delta w
            input_copy.remove(x)
        error = compute_error_function([input_data, expected_output], network)

        # ACA!
        print(error)

        if error < min_error:
            min_error = error
            network.update_layer_weights()
        i += 1
    return min_error

