import numpy as np


def euclidean(a, b):
    a = np.array(a)
    b = np.array(b)
    return np.linalg.norm(a - b)
