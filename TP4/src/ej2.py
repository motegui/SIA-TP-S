import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from TP4.src.ojaUtils import *
from TP4.src.oja import oja
from TP3.src.theta_functions import lineal_theta
from TP4.config import config
from TP4.src.standarize import standardize
from TP3.src.utils import random_initialize_weight


def main():
    input_data = pd.read_csv('/Users/lucho/Desktop/Repos/SIA-TP-S/TP4/data/europe.csv')
    input_data = input_data[
        ['Country', 'Area', 'GDP', 'Inflation', 'Life.expect', 'Military', 'Pop.growth', 'Unemployment']].values

    input_data = standardize(np.array(input_data)[:, 1:].astype(float))

    w, w_evol = oja(
        np.array(input_data).transpose(),
        random_initialize_weight,
        config.get("oja").get("limit"),
        config.get("oja").get("step"),
        lineal_theta
    )

    obtained_vs_expected(w_evol, [0.125, -0.501, 0.407, -0.483, 0.188, -0.476, 0.272])  # Pesos de la libreria


    variables = ['Area', 'GDP', 'Inflation', 'Life.expect', 'Military', 'Pop.growth', 'Unemployment']
    w_sorted = sorted(w)
    variables_sorted = [x for _, x in sorted(zip(w, variables))]
    plt.figure(figsize=(15, 15))
    plt.bar(range(len(w_sorted)), w_sorted)
    plt.tick_params(axis='y', labelsize=14)
    plt.xticks(range(len(w_sorted)), variables_sorted, rotation=40, fontsize=14)
    plt.xlabel('Variables', fontsize=18)
    plt.ylabel('Weights', fontsize=18)
    plt.title('Bar graph of variables sorted by weight', fontsize=24)
    plt.show()

    # grafico simil al PCA con pc1

    input_data = pd.read_csv('/Users/lucho/Desktop/Repos/SIA-TP-S/TP4/data/europe.csv')
    country_variables = input_data[
        ['Area', 'GDP', 'Inflation', 'Life.expect', 'Military', 'Pop.growth', 'Unemployment']].values
    country_variables = standardize(country_variables)
    country_variables = np.array(country_variables).transpose()

    pc1_per_country = [sum(np.multiply(i, w)) for i in country_variables]

    countries = input_data[['Country']].values.flatten()
    plt.figure(figsize=(15, 15))
    plt.bar(countries, pc1_per_country, color=(0.7, 0.7, 1, 0.5))
    plt.xticks(rotation=90, fontsize=14)
    plt.title('PC1 Index', fontsize=20)
    plt.ylabel('PC1', fontsize=14)
    plt.grid(axis='y')

    plt.show()


if __name__ == '__main__':
    main()
