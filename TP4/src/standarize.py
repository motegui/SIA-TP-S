import numpy as np
from scipy.stats import zscore


def standardize(data):
    data_standard = []
    for d in data:
        mean = np.mean(d[1:])
        std = np.std(d[1:])
        w1 = [d[0]]
        w2 = ((d[1:] - mean) / std).tolist()
        t = w1 + w2
        data_standard.append(t)

    return data_standard

