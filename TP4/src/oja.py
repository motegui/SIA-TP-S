import math
import os
import random

import numpy as np


def oja(input_data, initialize_weight, limit, step, epsilon, theta):
    i = 0
    w = initialize_weight(len(input_data[0])-1)
    min_error = math.inf
    w_min = None

    while min_error > epsilon and i < limit:
        u = random.randint(0, len(input_data) - 1)  # u es mu
        x = input_data[u]
        h = sum(np.multiply(x, w))  # compute
        o = theta(h)  # compute activation
        delta_w = oja_rule(o, x, step, w)
        w += delta_w
        i += 1
        print(w)
    return w_min, min_error


def oja_rule(o, x, step, w):
    o_x = np.multiply(o,x)
    oo = o**2
    o_w = np.multiply(oo, w)
    return step * (o_x - o_w)
    # return step*(o*x - (o**2) * w)