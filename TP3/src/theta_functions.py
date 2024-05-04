import numpy as np

from TP3.config import config


def staggered_theta(value):
    return 1 if value >= 0 else -1


def lineal_theta(value):
    return value


def lineal_prime_theta(value):
    return 1


BETA = config.get("beta")


def hyp_tan_theta(value):
    return np.tanh(BETA * value)


def hyp_tan_prime_theta(value):
    return BETA * (1 - np.square(hyp_tan_theta(value)))
    # return BETA * (1 - np.square(np.tanh(value))) todo por si quieren fijarse si asi anda!


def logistic_theta(value):
    return 1 / (1 + np.exp(-2 * BETA * value))


def logistic_prime_theta(value):
    return 2 * BETA * logistic_theta(value) * (1 - logistic_theta(value))


thetas = {
    "logistic": logistic_theta,
    "tanh": hyp_tan_theta,
    "lineal": lineal_theta,
    "staggered": staggered_theta
}

prime_thetas = {
    "logistic": logistic_prime_theta,
    "tanh": hyp_tan_prime_theta,
    "lineal": lineal_prime_theta
}
