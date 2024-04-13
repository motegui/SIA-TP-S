import numpy as np


def decreciente(prob_inicial, generacion, factor):
    return prob_inicial * np.exp(-factor * generacion + factor)


def creciente(prob_inicial, generacion, factor):
    if prob_inicial * np.exp(factor * generacion - factor) > 1:
        return 1
    return prob_inicial * np.exp(factor * generacion - factor)
