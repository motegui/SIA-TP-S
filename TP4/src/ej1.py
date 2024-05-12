import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

from TP4.src.kohonen import kohonen, calculate_u_matrix
from TP4.src.distance import euclidean
from TP4.src.radius import constant
import seaborn as sns
from TP4.src.standarize import standardize


def main():
    input_data = pd.read_csv('/Users/pazaramburu/Desktop/SIA-TP-S/TP4/data/europe.csv')
    input_data = input_data[
        ['Country', 'Area', 'GDP', 'Inflation', 'Life.expect', 'Military', 'Pop.growth', 'Unemployment']].values

    input_data = standardize(input_data)
    network = kohonen(input_data, 3, 2, euclidean, constant, 'input data', 0.1, 1)

    t = network.test(input_data)
    m = t[0].astype(float)
    # plt.imshow(m, cmap='hot', interpolation='nearest')
    # plt.colorbar()
    colors = [(0, 0, 0), (1, 0.2, 0), (1, 0, 0)]  # Negro al rojo

    # Crear el mapa de colores personalizado
    cmap = LinearSegmentedColormap.from_list('custom', colors)
    sns.heatmap(t[0].astype(float), annot=True, cmap=cmap, vmin=np.min(t[0].astype(float)),
                vmax=np.max(t[0].astype(float)))
    plt.title("heatmap")
    plt.show()

    u_matrix = calculate_u_matrix(network)
    u_cmap = LinearSegmentedColormap.from_list('custom', [(0.15, 0.15, 0.15), (1, 1, 1)])
    sns.heatmap(u_matrix, annot=True, cmap=u_cmap, vmin=np.max(u_matrix),
                vmax=np.min(u_matrix))
    plt.title("Matriz U")
    plt.show()

    print(t[1])


if __name__ == '__main__':
    main()

# Belgium  Croatia  Denmark  Estonia  Netherlands  Slovakia  Slovenia  Switzerland
#
# Finland  Germany  Italy  Norway  Poland  Spain  Sweden  Ukraine
