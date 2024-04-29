import math
import random

import numpy as np
from normalization import *


def staggered_perceptron(input_data, expected_output, initialize_weight, compute_error_function, limit, step):
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
        error = compute_error_function([input_data, expected_output], w)
        if error < min_error:
            min_error = error
            w_min = w.copy()
        i += 1
    return w_min, min_error


def lineal_nonlineal_perceptron(input_data, expected_output, initialize_weight, compute_error_function, limit, step,
                                epsilon, theta, theta_prime, min_max):
    i = 0
    w = initialize_weight(len(input_data[0]))
    min_error = math.inf
    w_min = None
    while min_error > epsilon and i < limit:
        u = random.randint(0, len(input_data) - 1)  # u es mu
        x = [1] + input_data[u]
        h = sum(np.multiply(x, w))  # compute
        o = theta(h)  # compute activation
        # delta_w = new_formula
        delta_w = np.multiply(step * (expected_output[u] - o) * theta_prime(h), x)
        w += delta_w
        error = compute_error_function([input_data, expected_output], w, theta, min_max)
        if error < min_error:
            min_error = error
            w_min = w.copy()
        i += 1
    return w_min, min_error


def random_initialize_weight(dim):
    return [random.random() for _ in range(dim + 1)]


def compute_error(data, w, theta, min_max):
    t = np.sum(np.square(np.subtract(data[1], real_output(data[0], w, theta))))
    return 0.5 * t


def compute_error_nonlinear(data, w, theta, min_max):
    input_data, expected_output = data
    # unormalized_input = np.interp(input_data, (0, 1), (min_max[0], min_max[1])).tolist()
    # unormalized_output = denormalize(expected_output, min_max[2], min_max[3])
    predicted_output = real_output(input_data, w, theta)
    # unormalized_predicted = denormalize(predicted_output, min_max[2], min_max[3])
    error = np.sum(np.square(np.subtract(expected_output, predicted_output)))
    return error * 0.5


def test_error(data, w, theta, min_max):
    input_data, expected_output = data
    predicted_output = real_output(input_data, w, theta)
    unormalized_predicted = denormalize(predicted_output, min_max[0], min_max[1])
    error = np.sum(np.square(np.subtract(expected_output, unormalized_predicted)))
    return error * 0.5


def real_output(input_data, w, theta):
    t = [theta(sum(np.multiply([1] + x, w))) for x in input_data]
    return t


def staggered_theta(value):
    return 1 if value >= 0 else -1


def lineal_theta(value):
    return value


def lineal_prime_theta(value):
    return 1


BETA = 1


def hyp_tan_theta(value):
    return np.tanh(BETA * value)


def hyp_tan_prime_theta(value):
    return BETA * (1 - np.square(hyp_tan_theta(value)))


def logistic_theta(value):
    return 1 / (1 + np.exp(-2 * BETA * value))


def logistic_prime_theta(value):
    return 2 * BETA * logistic_theta(value) * (1 - logistic_theta(value))
