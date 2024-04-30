import numpy as np

from utils import *
import pandas as pd
from normalization import *

from TP3.config import config

thetas = {
    "logistic": logistic_theta,
    "tanh": hyp_tan_theta
}

prime_thetas = {
    "logistic": logistic_prime_theta,
    "tanh": hyp_tan_prime_theta
}

def main():
    df = pd.read_csv('/Users/lucho/Desktop/Repos/SIA-TP-S/TP3/data/TP3-ej2-conjunto.csv')

    x_values = df[['x1', 'x2', 'x3']].values
    y_values = df['y'].values
    error_test, error_train = kfold_cross_validation([x_values, y_values], thetas.get(config.get("theta").get("name")),
                                                     prime_thetas.get(config.get("theta").get("name")), config.get("K"))
    print(error_test, "\n", error_train)

if __name__ == '__main__':
    main()
