from TP3.config import config
from TP3.src.perceptron import *
from TP3.src.utils import *


def kfold_cross_validation(data, theta, prime_theta, k):
    n = len(data[0])
    avg_size = n // k  # Average size of each part
    remainder = n % k  # Number of parts with one extra element

    x_values = data[0]
    denormalize_min = min(data[1])
    denormalize_max = max(data[1])
    min_max = [denormalize_min, denormalize_max]

    if config.get("theta").get("name") != 'lineal':
        y_values = normalize(data[1], config.get("theta").get("miny"), config.get("theta").get("maxy"))
    else:
        y_values = data[1]
        min_max = None

    splitted_x = [x_values[i * avg_size + min(i, remainder):(i + 1) * avg_size + min(i + 1, remainder)] for i in
                  range(k)]
    splitted_y = [y_values[i * avg_size + min(i, remainder):(i + 1) * avg_size + min(i + 1, remainder)] for i in
                  range(k)]

    error_testing_set = []
    error_training_set = []

    for fold in range(k):
        x_train = np.concatenate(splitted_x[:fold] + splitted_x[fold + 1:]).tolist()
        y_train = np.concatenate(splitted_y[:fold] + splitted_y[fold + 1:]).tolist()

        # Entreno con x_train, y_train
        [w, err_train] = lineal_nonlineal_perceptron(x_train, y_train, random_initialize_weight, compute_error,
                                                     config.get("limit"), config.get("step"), config.get("epsilon"),
                                                     theta, prime_theta)

        x_test = splitted_x[fold].tolist()
        if config.get("theta").get("name") != 'lineal':
            y_test = denormalize(splitted_y[fold], min_max[0], min_max[1])
        else:
            y_test = splitted_y[fold]

        err_test = test_error([x_test, y_test], w, theta, min_max)
        error_testing_set.append(err_test)
        error_training_set.append(err_train)
    return [error_training_set, error_testing_set]
