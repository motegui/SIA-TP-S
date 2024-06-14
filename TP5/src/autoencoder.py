import random
import numpy as np
from matplotlib import pyplot as plt

from TP3.src.Network import Network, layer_n_neurons, create_weighted_network
from TP3.src.Layer import Layer
from TP3.src.Neuron import Neuron
from TP3.src.normalization import normalize
from TP3.src.perceptron import multilayer_perceptron
from TP3.src.theta_functions import hyp_tan_theta, hyp_tan_prime_theta, logistic_theta, logistic_prime_theta, \
    lineal_theta, lineal_prime_theta
from TP3.src.utils import compute_error_multilayer
from TP4.src.hopfieldUtils import find_most_orthonormal_vectors
from TP5.src.utils import get_letters, test_network, get_labels_by_letters


def autoencoder(input_data, output_data):
    # random.shuffle(letters_pattern)
    layer1 = layer_n_neurons(35, hyp_tan_theta, hyp_tan_prime_theta)
    layer2 = layer_n_neurons(10, hyp_tan_theta, hyp_tan_prime_theta)
    layer3 = layer_n_neurons(25, hyp_tan_theta, hyp_tan_prime_theta)
    layer4 = layer_n_neurons(2, hyp_tan_theta, hyp_tan_prime_theta, is_latent=True)
    layer5 = layer_n_neurons(10, hyp_tan_theta, hyp_tan_prime_theta)
    layer6 = layer_n_neurons(25, hyp_tan_theta, hyp_tan_prime_theta)
    layer7 = layer_n_neurons(35, hyp_tan_theta, hyp_tan_prime_theta)
    layer8 = layer_n_neurons(2, hyp_tan_theta, hyp_tan_prime_theta)
    layer9 = layer_n_neurons(20, hyp_tan_theta, hyp_tan_prime_theta)
    layer10 = layer_n_neurons(30, hyp_tan_theta, hyp_tan_prime_theta)
    layer11 = layer_n_neurons(35, hyp_tan_theta, hyp_tan_prime_theta)
    n = Network([layer2, layer4, layer5, layer7])

    n.initialize(input_count=35)

    nor = [[-1 if elemento == 0 else elemento for elemento in fila] for fila in output_data]

    error = multilayer_perceptron(input_data, nor, compute_error_multilayer, 20000, 0.5, n)
    print(n.forward_propagation(input_data[1]))
    print(input_data[1])
    return n


def plot_latent_space(input_data, encoder):

    labels = get_labels_by_letters(input_data)
    x_component = []
    y_component = []

    for data in input_data:
        latent_cords = encoder.forward_propagation(data)
        x_component.append(latent_cords[0])
        y_component.append(latent_cords[1])

    # Crear la gráfica
    plt.figure(figsize=(10, 6))
    plt.scatter(x_component, y_component)

    # Añadir etiquetas a cada punto
    for i in range(len(x_component)):
        plt.text(x_component[i], y_component[i], labels[i], fontsize=12, ha='right')

    # Añadir título y etiquetas de los ejes
    plt.title('Gráfico de Puntos con Etiquetas')
    plt.xlabel('Componente X')
    plt.ylabel('Componente Y')

    # Mostrar la gráfica
    plt.grid(True)
    plt.show()
