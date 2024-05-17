import numpy as np
import scipy as sp


def standardize(data):
    data_standard = []
    for i in range(len(data[0])):
        mean = np.mean(data[:,i])
        std = np.std(data[:,i])
        w2 = ((data[:, i] - mean) / std).tolist()

    return data_standard

