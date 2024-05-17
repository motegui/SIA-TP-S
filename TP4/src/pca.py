from matplotlib.colors import LinearSegmentedColormap
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA

import seaborn as sns

from matplotlib import pyplot as plt
from TP4.src.radius import constant
from TP4.src.distance import euclidean
from TP4.src.kohonen import kohonen
from TP4.src.standarize import standardize


def plot(means, std):
    name = ['Area', 'GDP', 'Inflation', 'Life Expect', 'Military', 'Pop Growth', 'Unemployment']
    color = [(1, 0.7, 0.7, 0.5),  # Rosa pastel transparente
             (0.7, 1, 0.7, 0.5),  # Verde claro pastel transparente
             (0.7, 0.7, 1, 0.5),  # Azul claro pastel transparente
             (1, 0.85, 0.5, 0.5),  # Naranja claro pastel transparente
             (0.5, 1, 1, 0.5),  # Cyan pastel transparente
             (1, 0.5, 1, 0.5),  # Magenta pastel transparente
             (1, 0.9, 0.7, 0.5)]  # Melocotón pastel transparente

    # Crear un gráfico de barras con las medias
    plt.bar(name, means, yerr=std, capsize=5, color=color)

    # Etiquetas y título
    plt.xlabel('Input data')
    plt.ylabel('Data mean')
    plt.title('Mean and std with no standarize')

    # Mostrar el gráfico
    plt.show()


def main():

    input_data = pd.read_csv('/Users/nicolastordomar/Desktop/SIA-TP-S/TP4/data/europe.csv')
    input_data = input_data[
        ['Country', 'Area', 'GDP', 'Inflation', 'Life.expect', 'Military', 'Pop.growth', 'Unemployment']].values



    means = [np.mean(input_data[:,i]) for i in range(1,len(input_data[0]))]
    std = [np.std(input_data[:,i]) for i in range(1,len(input_data[0]))]

    plot(means,std)

    #stadarized!
    input_data = np.array(standardize(input_data))
    means = [np.mean(input_data[:,i].astype(float)) for i in range(1,len(input_data[0]))]
    std = [np.std(input_data[:,i].astype(float)) for i in range(1,len(input_data[0]))]

    plot(means, std)


    print(input_data)
    print(input_data[:,1:])
    pca = PCA(n_components=1)
    componentes_principales = pca.fit_transform(np.transpose(input_data[:, 1:].astype(float)))
    print(componentes_principales)


#
#
# input_data = standardize(input_data)
# network = kohonen(input_data, 2, 10000, euclidean, constant, 'input data', 0.1, 1)
#
# t = network.test(input_data)
# colors = [(256, 256, 256), (1, 0, 0)]  # Negro al rojo
#
# # Crear el mapa de colores personalizado
# cmap = LinearSegmentedColormap.from_list('custom', colors)
# ax = sns.heatmap(t[0].astype(float), cmap=cmap, vmin=np.min(t[0].astype(float)), vmax=np.max(t[0].astype(float)))
# plt.colorbar()
# plt.show()
#
# print(t[0])
# print(t[1])
#

if __name__ == '__main__':
    main()
