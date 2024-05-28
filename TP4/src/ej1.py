import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

from TP4.config import config
from utils import *
from TP4.src.kohonen import kohonen, calculate_u_matrix, calculate_u_matrix_by_variable
from TP4.src.distance import euclidean
from TP4.src.radius import constant, decreasing
import seaborn as sns
from TP4.src.standarize import standardize
import plotly.graph_objects as go


def main():
    csv_data = pd.read_csv('/Users/lucho/Desktop/Repos/SIA-TP-S/TP4/data/europe.csv')
    input_data = csv_data[
        ['Area', 'GDP', 'Inflation', 'Life.expect', 'Military', 'Pop.growth', 'Unemployment']].values

    countries = np.array(csv_data['Country'].values)

    input_data = standardize(input_data)
    input_data = np.transpose(input_data)
    input_data = [list(np.concatenate([np.array([countries[i]]), input_data[i].astype(float)])) for i in
                  range(len(input_data))]
    #print(input_data)
    k = config.get("kohonen").get("k")
    network = kohonen(input_data, k, config.get("kohonen").get("limit"), euclidean, decreasing, 'input data', 0.1, 2)

    t = network.test(input_data)
    m = t[0].astype(float)
    plt.imshow(m, cmap='hot', interpolation='nearest')
    plt.colorbar()
    colors = [(0, 0, 0), (1, 0.2, 0), (1, 0, 0)]  # Negro al rojo

    #heatmap(mapa interactivo)
    # cmap = LinearSegmentedColormap.from_list('custom', colors)
    # colorscale = [[0, 'red'], [1, 'black']]
    # country_matrix = [[f"{country}<br>{int(value)}" for country, value in zip(countries, row_values)] for
    #                   countries, row_values in zip(t[1], m)]
    # heatmap = go.Heatmap(z=m, colorscale=colorscale, text=country_matrix, hoverinfo='text')
    # layout = go.Layout(title="Heatmap with Country Names and Total Quantity")
    # fig = go.Figure(data=[heatmap], layout=layout)
    # fig.show()

    #heatmap no interactivo ( funciona, no puedo hacer que los nombres de los paises se vean clean)
    cmap = LinearSegmentedColormap.from_list('custom', colors)
    annotations = []
    for countries, row_values in zip(t[1], m):
        row_annotations = []
        for country_list, value in zip(countries, row_values):
            if country_list:
                country_str = country_list.replace('  ', '\n')
                annotation = f"{country_str}\n({int(value)})"
            else:
                annotation = f"({int(value)})"
            row_annotations.append(annotation)
        annotations.append(row_annotations)

    annotations = np.array(annotations)

    print(annotations)
    # print(annotations)
    plt.figure(figsize=(12, 10))  # Ajusta el tamaño de la figura
    sns.heatmap(m, annot=annotations, fmt='', cmap=cmap, cbar_kws={'label': 'Values'})
    plt.title("Heatmap with Country Names and Quantities")
    plt.show()

    #matriz u
    u_matrix = calculate_u_matrix(network)
    u_cmap = LinearSegmentedColormap.from_list('custom', [(0.15, 0.15, 0.15), (1, 1, 1)])
    sns.heatmap(u_matrix, annot=True, cmap=u_cmap, vmin=np.max(u_matrix),
                vmax=np.min(u_matrix))
    plt.title("Matriz U")
    plt.show()

    #print(t[1])
    #-------
    #diccionario para hacer matriz de coincidencias
    # coincidence_matrix = {}
    #
    # # Ejecutar el algoritmo de Kohonen 100 veces
    # for _ in range(100):
    #     network = kohonen(input_data, 3, 2, euclidean, constant, 'input data', 0.1, 1)
    #
    #     # obtengo los grupos de paises para cada iteracion
    #     _, matrix = network.test(input_data)
    #
    #     for row in matrix:
    #         for associated_countries in row:
    #             associated_countries_list = [country.replace(' ', '') for country in associated_countries.split('  ')]
    #             for country_it1 in associated_countries_list:
    #                 for country_it2 in associated_countries_list:
    #                     coincidence_matrix.setdefault(country_it1, {})
    #                     coincidence_matrix[country_it1].setdefault(country_it2, 0)
    #                     coincidence_matrix[country_it1][country_it2] += 1

    # def print_sorted_table(data):
    #     # Extract and sort headers
    #     headers = sorted(data.keys())
    #     if not headers:
    #         print("Empty table")
    #         return
    #
    #     #determino el maximo ancho para el formato
    #     max_key_length = max(len(str(key)) for key in headers)
    #     max_val_length = max(len(str(val)) for row in data.values() for val in row.values())
    #
    #     #calculo el ancho de la columna
    #     col_width = max(max_key_length, max_val_length)
    #
    #     #imprimo el header de la columna
    #     header_row = f"{'':>{col_width}} " + " ".join(f"{header:>{col_width}}" for header in headers)
    #     print(header_row)
    #
    #     for row_header in headers:
    #         row = data[row_header]
    #         row_str = f"{row_header:>{col_width}} " + " ".join(
    #             f"{row.get(col_header, ''):>{col_width}}" for col_header in headers)
    #         print(row_str)
    #
    # for country1 in coincidence_matrix.keys():
    #     for country2 in coincidence_matrix.keys():
    #         coincidence_matrix[country1].setdefault(country2, 0)
    # print_sorted_table(coincidence_matrix)
    # pass

    #u matrix by variable
    for index, name in enumerate(['Area', 'GDP', 'Inflation', 'Life.expect', 'Military', 'Pop.growth', 'Unemployment']):
        u_matrix = calculate_u_matrix_by_variable(network, index)
        u_cmap = LinearSegmentedColormap.from_list('custom', [(0.15, 0.15, 0.15), (1, 1, 1)])
        sns.heatmap(u_matrix, annot=True, cmap=u_cmap, vmin=np.max(u_matrix),
                    vmax=np.min(u_matrix))
        plt.title("Matriz U para " + name)
        plt.show()


if __name__ == '__main__':
    main()
