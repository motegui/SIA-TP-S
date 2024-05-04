import numpy as np


def gradient_descend(step, delta, output):
    t = np.multiply(step * delta, output).tolist()
    return t
