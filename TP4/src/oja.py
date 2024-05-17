import math
import os
import random

import numpy as np


def oja(input_data, initialize_weight, limit, step, epsilon, theta):
    i = 0
    w = initialize_weight(len(input_data[0]) - 1)
    min_error = math.inf
    w_min = None

    while min_error > epsilon and i < limit:
        u = random.randint(0, len(input_data) - 1)  # u es mu
        x = input_data[u]
        h = sum(np.multiply(x, w))  # Excitation
        o = theta(h)  # Compute activation
        delta_w = oja_rule(o, x, step, w)  # step*(o*x - o^2*w)
        w += delta_w
        i += 1
    return w


def oja_rule(o, x, step, w):
    return step * (np.multiply(o, x) - np.multiply(o ** 2, w))
