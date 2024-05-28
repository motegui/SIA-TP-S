import matplotlib.pyplot as plt
import numpy as np

from TP4.src.hopfield import hopfield
from TP4.src.hopfieldUtils import *
from TP4.config import config


def main():
    # Printing all letters
    # for letter in letters:
    #     create_letter_plot(letter)

    # Finding the best 4 letters for Hopfield Algorithm
    flatten_letters = [get_flatten_letter(letter) for letter in letters]
    best_group, best_group_ortho = find_most_orthonormal_vectors(flatten_letters, 4)
    for letter in best_group[-1]:
        create_letter_plot(get_matrix_letter(letter))  # Best group is C F I Z

    # Checking evolution from a noisy letter (Z)
    res, evolution, energy = hopfield(
        [get_flatten_letter(C), get_flatten_letter(F), get_flatten_letter(I), get_flatten_letter(Z)],
        config.get("hopfield").get("limit"),
        get_flatten_letter(generate_noice(Z, 0.3)))
    energy_plot(energy)
    create_letter_plot(get_matrix_letter(res))
    for ev in evolution:
        create_letter_plot(get_matrix_letter(ev))

    # Energy plot (Z)
    res, evolution, energy = hopfield(
        [get_flatten_letter(C), get_flatten_letter(F), get_flatten_letter(I), get_flatten_letter(Z)],
        config.get("hopfield").get("limit"),
        get_flatten_letter(generate_noice(Z, 0.3)))
    energy_plot(energy)

    # Not orthogonal
    flatten_letters = [get_flatten_letter(letter) for letter in letters]
    worst_group, worst_prod = find_least_orthonormal_vectors(flatten_letters, 4)
    for worst in worst_group:
        create_letter_plot(get_matrix_letter(worst))
    res, evolution, energy = hopfield(
        [get_flatten_letter(C), get_flatten_letter(D), get_flatten_letter(O), get_flatten_letter(Q)],
        5000,
        get_flatten_letter(generate_noice(C, 0)))
    for ev in evolution:
        create_letter_plot(get_matrix_letter(ev))


if __name__ == '__main__':
    main()
