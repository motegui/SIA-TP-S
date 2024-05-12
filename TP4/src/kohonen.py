import random
from typing import *
from Network import *
from TP4.src.distance import euclidean


def kohonen(
        input_data: list,
        k: int,
        limit: int,
        distance_function: Callable,
        radius: Callable,
        initialize_weight_type: str,
        learning_rate: float,
        batch_size: int
) -> Network:
    network = Network(input_data, k, initialize_weight_type, distance_function)
    i = 0

    while i < limit:
        batch_idx = 1
        input_copy = input_data.copy()
        while batch_idx < batch_size:
            u = random.randint(0, len(input_copy) - 1)
            x = input_copy[u]
            winner_index = network.get_winner_neuron_index(x[1:])
            network.update_weights(winner_index, radius(i), learning_rate, x)
            batch_idx += 1

        i += 1
    return network


def calculate_u_matrix(network: Network) -> np.ndarray:
    u_matrix = np.zeros_like(network.matrix, dtype=float)
    for i in range(len(network.matrix)):
        for j in range(len(network.matrix[0])):
            neighbors = get_neighbors(network, i, j)
            distances = []
            for neighbor in neighbors:
                #cannot use the network's distance bc for u matrix we must use the euclidean
                distances.append(euclidean(network.matrix[i][j].weights, neighbor.weights))
            u_matrix[i][j] = np.mean(distances)
    return u_matrix


def get_neighbors(network: Network, i: int, j: int) -> list:
    neighbors = []
    #itero por los vecinos
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            new_i = i + dx
            new_j = j + dy
            #controlo q no se vacha del limite
            if 0 <= new_i < len(network.matrix) and 0 <= new_j < len(network.matrix[0]):
                neighbors.append(network.matrix[new_i][new_j])
    return neighbors
