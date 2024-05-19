import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from utils import *
from TP4.src.kohonen import kohonen, calculate_u_matrix
from TP4.src.distance import euclidean
from TP4.src.radius import constant
import seaborn as sns
from TP4.src.standarize import standardize
import plotly.graph_objects as go


def main():
    csv_data = pd.read_csv('/Users/motegui/Documents/GitHub/SIA-TP-S/TP4/data/europe.csv')
    input_data = csv_data[
        ['Area', 'GDP', 'Inflation', 'Life.expect', 'Military', 'Pop.growth', 'Unemployment']].values

    countries = np.array(csv_data['Country'].values)

    input_data = standardize(input_data)
    input_data = np.transpose(input_data)
    input_data = [list(np.concatenate([np.array([countries[i]]), input_data[i].astype(float)])) for i in
                  range(len(input_data))]
    #print(input_data)

    network = kohonen(input_data, 3, 2, euclidean, constant, 'input data', 0.1, 1)

    t = network.test(input_data)
    m = t[0].astype(float)
    plt.imshow(m, cmap='hot', interpolation='nearest')
    plt.colorbar()
    colors = [(0, 0, 0), (1, 0.2, 0), (1, 0, 0)]  # Negro al rojo

    #Crear el mapa de colores personalizado (mapa interactivo)
    cmap = LinearSegmentedColormap.from_list('custom', colors)
    colorscale = [[0, 'red'], [1, 'black']]
    country_matrix = [[f"{country}<br>{int(value)}" for country, value in zip(countries, row_values)] for
                      countries, row_values in zip(t[1], m)]
    heatmap = go.Heatmap(z=m, colorscale=colorscale, text=country_matrix, hoverinfo='text')
    layout = go.Layout(title="Heatmap with Country Names and Total Quantity")
    fig = go.Figure(data=[heatmap], layout=layout)
    fig.show()

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

if __name__ == '__main__':
    main()
