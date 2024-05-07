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
    for i in range(len(input_data)):
        forward = network.updated_forward_propagation(input_data[i])
        t = np.square(np.array(forward) - np.array(expected_output[i]))

        errors.append(sum(t))
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


def create_numbers_with_noise(clean_numbers, qty_by_number):
    numbers_with_noise = []
    results = []
    actual_numbers = []
    for i, number in enumerate(clean_numbers):
        for _ in range(qty_by_number):
            clean_matrix = np.array(number.split(), dtype=int).reshape(5, 7)
            noise = np.random.normal(0, 0.3, (5, 7))  # Gaussian noise with mean 0 and standard deviation 0.1
            matrix_with_noise = clean_matrix + noise
            matrix_with_noise = (matrix_with_noise >= 0.5).astype(int)  # Convert values >= 0.5 to 1, otherwise to 0
            numbers_with_noise.append(matrix_with_noise.flatten())
            result = [0] * 10
            result[i] = 1
            results.append(result)
            actual_numbers.append(i)
    return [[t.tolist() for t in numbers_with_noise], results, actual_numbers]


def get_expected_digits():
    results = []
    for i in range(0, 10):
        out = [0] * 10
        out[i] = 1
        results.append(out)
    return results


def get_clean_matrix(clean_numbers):
    result = []
    for number in clean_numbers:
        result.append(np.array(number.split(), dtype=int).reshape(5, 7).flatten().tolist())
    return result


def transform_csv_to_list(csv_file):
    with open(csv_file, 'r') as file:
        lines = file.readlines()

    groups = []
    current_group = []
    for line in lines:
        line = line.strip()  # Remove leading and trailing whitespace
        if line:
            current_group.append(line)
            if len(current_group) == 7:
                groups.append('\n'.join(current_group))
                current_group = []

    return groups


def shuffle_arrays(x, y):
    x = np.array(x)
    y = np.array(y)
    perm = np.random.permutation(len(x))
    x_shuffled = x[perm]
    y_shuffled = y[perm]
    return x_shuffled.tolist(), y_shuffled.tolist()
