import random
import numpy as np
from matplotlib import pyplot as plt

from TP3.src.Network import Network, layer_n_neurons
from TP3.src.perceptron import multilayer_perceptron
from TP3.src.theta_functions import hyp_tan_theta, hyp_tan_prime_theta, lineal_theta, lineal_prime_theta
from TP3.src.utils import compute_error_multilayer
from TP5.src.utils import get_labels_by_letters


def autoencoder(input_data, output_data):
    layer1 = layer_n_neurons(25, lineal_theta, lineal_prime_theta)
    layer2 = layer_n_neurons(25, lineal_theta, lineal_prime_theta)
    layer3 = layer_n_neurons(25, lineal_theta, lineal_prime_theta)
    layer4 = layer_n_neurons(25, lineal_theta, lineal_prime_theta)
    layer5 = layer_n_neurons(2, lineal_theta, lineal_prime_theta, is_latent=True)
    layer6 = layer_n_neurons(25, lineal_theta, lineal_prime_theta)
    layer7 = layer_n_neurons(35, hyp_tan_theta, hyp_tan_prime_theta)
    layer8 = layer_n_neurons(35, hyp_tan_theta, hyp_tan_prime_theta)
    layer9 = layer_n_neurons(35, hyp_tan_theta, hyp_tan_prime_theta)
    layer10 = layer_n_neurons(35, hyp_tan_theta, hyp_tan_prime_theta)

    n = Network([layer1, layer2, layer5, layer8, layer9, layer10])

    n.initialize(input_count=35)
    nor = [[-1 if elemento == 0 else elemento for elemento in fila] for fila in output_data]

    error = multilayer_perceptron(input_data, nor, compute_error_multilayer, 1, 0.5, n)
    print(n.get_weights())
    print(input_data[1])
    return n


def plot_latent_space(clean_letters, input_data, encoder):

    labels = get_labels_by_letters(clean_letters)
    x_component = []
    y_component = []

    for data in input_data:
        latent_cords = encoder.forward_propagation(data)
        x_component.append(latent_cords[0])
        y_component.append(latent_cords[1])

    plt.figure(figsize=(10, 6))
    plt.scatter(x_component, y_component)

    for i in range(len(x_component)):
        plt.text(x_component[i], y_component[i], labels[i], fontsize=12, ha='right')

    plt.title('Gráfico de Puntos con Etiquetas')
    plt.xlabel('Componente X')
    plt.ylabel('Componente Y')

    plt.grid(True)
    plt.show()