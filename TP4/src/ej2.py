import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

from TP4.src.oja import oja
from TP3.src.theta_functions import lineal_theta
from TP4.config import config
from TP4.src.standarize import standardize
from TP3.src.utils import random_initialize_weight


def main():
    input_data = pd.read_csv('/Users/pazaramburu/Desktop/SIA-TP-S/TP4/data/europe.csv')
    input_data = input_data[
        ['Country', 'Area', 'GDP', 'Inflation', 'Life.expect', 'Military', 'Pop.growth', 'Unemployment']].values

    input_data = standardize(np.array(input_data)[:, 1:].astype(float))

    w = oja(
        np.array(input_data).transpose(),
        random_initialize_weight,
        config.get("limit"),
        config.get("step"),
        config.get("epsilon"),
        lineal_theta
    )

    print(w)

    #grafico de mayor a menor peso
    variables = ['Area', 'GDP', 'Inflation', 'Life.expect', 'Military', 'Pop.growth', 'Unemployment']
    w_sorted = sorted(w, reverse=True)
    variables_sorted = [x for _, x in sorted(zip(w, variables), reverse=True)]
    plt.figure(figsize=(15, 15))
    plt.bar(range(len(w_sorted)), w_sorted)
    plt.tick_params(axis='y', labelsize=14)
    plt.xticks(range(len(w_sorted)), variables_sorted, rotation=40, fontsize=14)
    plt.xlabel('Variables', fontsize=18)
    plt.ylabel('Weights', fontsize=18)
    plt.title('Bar graph of variables sorted by weight', fontsize=24)
    plt.show()


if __name__ == '__main__':
    main()
