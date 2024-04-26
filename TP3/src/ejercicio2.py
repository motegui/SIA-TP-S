import numpy as np

from utils import *
import pandas as pd


def main():
    TRAINING_SIZE = 15

    df = pd.read_csv('/Users/motegui/Documents/GitHub/SIA-TP-S/TP3/data/TP3-ej2-conjunto.csv')

    x_values_train = df[['x1', 'x2', 'x3']].values
    y_values_train = df['y'].values

    # Normalizar los datos entre -1 y 1 utilizando la interpolación de NumPy
    x_values_train_normalized = np.interp(x_values_train, (x_values_train.min(), x_values_train.max()), (0, 1)).tolist()
    y_values_train_normalized = np.interp(y_values_train, (y_values_train.min(), y_values_train.max()), (0, 1)).tolist()

    # x_values_train = np.array(x_values[:])
    # y_values_train = np.array(y_values[:])

    # [w, err] = lineal_nonlineal_perceptron(x_values_train, y_values_train, random_initialize_weight, compute_error, 10000,
    #                                        0.02,
    #                                        0, lineal_theta, lineal_prime_theta)

    # El error dio muy alto por lo que no es lineal. A medida que agrandamos el training size da mas alto el error
    # normalized_data = np.interp(data, (min_val, max_val), (new_min, new_max))
    # normalized_data = np.interp(x_values_train, (min(x_values_train), max(x_values_train)), (-1, 1))

    randomNum1 = random.randint(0, len(x_values_train_normalized)-1)
    randomNum2 = random.randint(0, len(x_values_train_normalized)-1)
    randomNum3 = random.randint(0, len(x_values_train_normalized)-1)

    test_X = [x_values_train_normalized[randomNum1], x_values_train_normalized[randomNum2], x_values_train_normalized[randomNum3]]
    test_y = [y_values_train_normalized[randomNum1], y_values_train_normalized[randomNum2], y_values_train_normalized[randomNum3]]

    [w, err] = lineal_nonlineal_perceptron(test_X,
                                           test_y,
                                           random_initialize_weight, compute_error,
                                           100,
                                           0.1,
                                           0, logistic_theta, logistic_prime_theta)

    print('error is: ', err)

    # x_values_train = x_values[TRAINING_SIZE:]
    # y_values_train = y_values[TRAINING_SIZE:]



    for x, y in zip(x_values_train_normalized,
                    y_values_train_normalized):
        print(sum(np.multiply(w, [1] + x) - y))


if __name__ == '__main__':
    main()

