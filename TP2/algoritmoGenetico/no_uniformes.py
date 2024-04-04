import numpy as np


def decreciente(prob_inicial, generacion, factor):
    return prob_inicial * np.exp(-factor * generacion + factor)


def creciente(prob_inicial, generacion, factor):
    return prob_inicial * np.exp(factor * generacion - factor)
