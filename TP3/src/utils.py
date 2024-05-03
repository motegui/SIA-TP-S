import random
import numpy as np
from normalization import *


def random_initialize_weight(dim):
    return [random.random() for _ in range(dim + 1)]


def compute_error(data, w, theta):
    t = np.sum(np.square(np.subtract(data[1], real_output(data[0], w, theta))))
    return 0.5 * t


def compute_error_multilayer(data, network):
    input_data = data[0]
    expected_output = data[1]
    errors = []
    for input in input_data:
        for result in expected_output:
            forward = network.updated_forward_propagation(input)
            errors.append(sum(np.square(np.array(forward) - np.array(result))))
    return sum(errors) * 0.5


def test_error(data, w, theta, min_max=None):
    input_data, expected_output = data
    predicted_output = real_output(input_data, w, theta)
    if min_max is not None:
        unormalized_predicted = denormalize(predicted_output, min_max[0], min_max[1])
    else:
        unormalized_predicted = predicted_output
    error = np.sum(np.square(np.subtract(expected_output, unormalized_predicted)))
    return error * 0.5


# returns algorithm response
def real_output(input_data, w, theta):
    t = [theta(sum(np.multiply([1] + x, w))) for x in input_data]
    return t
