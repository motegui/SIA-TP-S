import math
import random

import numpy as np
from normalization import *
from TP3.config import config


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
                                epsilon, theta, theta_prime, min_max=None):
    if min_max is None:
        min_max = [config.get("theta").get("miny"), config.get("theta").get("maxy")]

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


def random_initialize_weight(dim):
    return [random.random() for _ in range(dim + 1)]


def compute_error(data, w, theta):
    t = np.sum(np.square(np.subtract(data[1], real_output(data[0], w, theta))))
    return 0.5 * t


def kfold_cross_validation(data, theta, prime_theta, k):
    n = len(data[0])
    avg_size = n // k  # Average size of each part
    remainder = n % k  # Number of parts with one extra element

    denormalize_min = min(data[1])
    denorlize_max = max(data[1])
    min_max = [denormalize_min, denorlize_max]

    x_values = data[0]
    y_values = normalize(data[1], config.get("theta").get("miny"), config.get("theta").get("maxy"))

    splitted_x = [x_values[i * avg_size + min(i, remainder):(i + 1) * avg_size + min(i + 1, remainder)] for i in
                  range(k)]
    splitted_y = [y_values[i * avg_size + min(i, remainder):(i + 1) * avg_size + min(i + 1, remainder)] for i in
                  range(k)]

    error_testing_set = []
    error_training_set = []

    for fold in range(k):
        x_train = np.concatenate(splitted_x[:fold] + splitted_x[fold + 1:]).tolist()
        y_train = np.concatenate(splitted_y[:fold] + splitted_y[fold + 1:]).tolist()

        x_test = splitted_x[fold].tolist()
        y_test = denormalize(splitted_y[fold], min_max[0], min_max[1])

        # Entreno con x_train, y_train
        [w, err_train] = lineal_nonlineal_perceptron(x_train, y_train, random_initialize_weight, compute_error,
                                                     config.get("limit"), config.get("step"), config.get("epsilon"),
                                                     theta, prime_theta, min_max)

        err_test = test_error([x_test, y_test], w, logistic_theta, min_max)
        error_testing_set.append(err_test)
        error_training_set.append(err_train)
    return [error_training_set, error_testing_set]


# def compute_error_nonlinear(data, w, theta):
#     input_data, expected_output = data
#     predicted_output = real_output(input_data, w, theta)
#     error = np.sum(np.square(np.subtract(expected_output, predicted_output)))
#     return error * 0.5


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
