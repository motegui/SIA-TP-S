import math
import random

import numpy as np


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


def random_initialize_weight(dim):
    return [random.random() for _ in range(dim + 1)]


def compute_error(data, w):
    t = np.sum(np.square(np.subtract(data[1], real_output(data[0], w))))
    return 0.5 * t


def real_output(input_data, w):
    t = [1 if sum(np.multiply([1] + x, w)) >= 0 else -1 for x in input_data]
    return t
