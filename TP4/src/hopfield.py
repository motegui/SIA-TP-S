import numpy as np
from hopfieldUtils import *
import copy
def hopfield(patterns, limit, input_pattern):
    N = len(patterns[0])
    K = np.array(patterns).transpose()
    W = (1.0 / N) * np.dot(K, K.transpose())
    energy = []
    np.fill_diagonal(W, 0)
    patterns = []
    i = 0
    S = input_pattern
    while i < limit:
        patterns.append(S)
        prev_S = np.copy(S)
        S = np.sign(np.dot(W, S)).tolist()
        energy.append(get_energy(W, S).copy())
        if np.array_equal(prev_S, S):
            break

        i += 1

    return S, patterns, energy
