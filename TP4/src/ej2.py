import numpy as np
import pandas as pd

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

    w = oja(
        np.array(input_data).transpose(),
        random_initialize_weight,
        config.get("limit"),
        config.get("step"),
        config.get("epsilon"),
        lineal_theta
    )

    print(w)


if __name__ == '__main__':
    main()
