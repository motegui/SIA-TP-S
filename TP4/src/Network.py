import math
import random
from Neuron import *
import numpy as np
from initializer import *

from utils import *


class Network:
    def __init__(self, input_data, k, initialize_weight_type, distance_function):  # Recibe las layers en orden
        self.matrix = initialize_matrix(input_data, k, initialize_weight_type)
        self.distance_function = distance_function

    def get_winner_neuron_index(self, data) -> tuple[int, int]:
        min_distance = math.inf
        winner_idx = (math.inf, math.inf)
        for j in range(len(self.matrix)):
            for i in range(len(self.matrix[0])):
                distance = self.distance_function(self.matrix[i][j].weights, data)
                if distance < min_distance:
                    min_distance = distance
                    winner_idx = (i, j)
        return winner_idx

    def update_weights(self, winner: tuple[int, int], x: list, radius: int, learning_rate: float):
        neurons = iterate_within_radius(self.matrix, winner, radius)
        for neuron in neurons:
            neuron.update_weights(x, learning_rate)

    def test(self, input_data):
        matrix = np.zeros_like(self.matrix)
        matrix_country = [[""] * len(self.matrix) for _ in range(len(self.matrix))]
        for input in input_data:
            idx = self.get_winner_neuron_index(input[1:])
            matrix[idx[0], idx[1]] += 1
            matrix_country[idx[0]][idx[1]] += ' ' + input[0] + ' '

        return matrix, matrix_country


def initialize_matrix(input_data, k, initialize_weight_type):
    if initialize_weight_type == 'RANDOM':
        weight_function = random_initializer
    else:
        weight_function = input_initializer

    matrix = [[0] * k for _ in range(k)]
    input_data_copy = input_data.copy()
    for i in range(k):
        for j in range(k):
            matrix[i][j] = Neuron(weight_function(input_data_copy), i, j)
    return matrix
