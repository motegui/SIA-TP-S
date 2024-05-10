import random
from typing import *
from Network import *


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
