import numpy as np


def euclidean(a, b):
    a = np.array(a).astype(float)
    b = np.array(b).astype(float)
    return np.linalg.norm(a - b)
