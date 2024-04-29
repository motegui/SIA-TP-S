import numpy as np

from utils import *
import pandas as pd
from normalization import *

def main():
    df = pd.read_csv('/Users/pazaramburu/Desktop/SIA-TP-S/TP3/data/TP3-ej2-conjunto.csv')

    x_values = df[['x1', 'x2', 'x3']].values
    y_values = df['y'].values

    # Normalizar los datos entre -1 y 1 utilizando la interpolación de NumPy
    x_min = x_values.min()
    x_max = x_values.max()
    y_min = y_values.min()
    y_max = y_values.max()
    # x_values_normalized = np.interp(x_values, (x_min, x_max), (-1, 1)).tolist()
    x_values = x_values.tolist()
    y_values_normalized = normalize(y_values, 0, 1)

    split_index = int(len(x_values) * 0.8)  # 80% de los datos para train
    x_train, x_test = x_values[:split_index], x_values[split_index:]
    y_train, y_test = y_values_normalized[:split_index], y_values_normalized[split_index:]

    #entrenamos el perceptron
    [w, err_train] = lineal_nonlineal_perceptron(x_train, y_train, random_initialize_weight, compute_error_nonlinear,
                                                 10000, 0.01, 0, logistic_theta, logistic_prime_theta,
                                                 [y_min, y_max])

    # rendimiento en conjunto train -> capacidad de aprendizaje
    print('Error en el conjunto de entrenamiento:', err_train)

    # rendimiento en el conjunto de prueba -> capacidad de generalizacion
    y_test = denormalize(y_test, y_min, y_max)
    err_test = test_error([x_test, y_test], w, logistic_theta, [y_min, y_max])
    print('Error en el conjunto de prueba:', err_test)


if __name__ == '__main__':
    main()
