from TP3.src.kfold import kfold_cross_validation
from TP3.src.theta_functions import thetas, prime_thetas
import pandas as pd

from TP3.config import config


def main():
    df = pd.read_csv('/Users/nicolastordomar/Desktop/SIA-TP-S/TP3/data/TP3-ej2-conjunto.csv')
    df = df.sample(frac=1)
    x_values = df[['x1', 'x2', 'x3']].values
    y_values = df['y'].values
    error_train, error_test = kfold_cross_validation([x_values, y_values], thetas.get(config.get("theta").get("name")),
                                                     prime_thetas.get(config.get("theta").get("name")), config.get("K"))
    print(error_train, "\n", error_test)


if __name__ == '__main__':
    main()
