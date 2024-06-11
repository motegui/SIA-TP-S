import random

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from itertools import combinations

A = [
    [-1, -1, 1, -1, -1],
    [-1, 1, -1, 1, -1],
    [1, 1, 1, 1, 1],
    [1, -1, -1, -1, 1],
    [1, -1, -1, -1, 1]
]

B = [[1, 1, 1, 1, -1],
     [1, -1, -1, -1, 1],
     [1, 1, 1, 1, -1],
     [1, -1, -1, -1, 1],
     [1, 1, 1, 1, -1]]

C = [[-1, 1, 1, 1, -1],
     [1, -1, -1, -1, 1],
     [1, -1, -1, -1, -1],
     [1, -1, -1, -1, 1],
     [-1, 1, 1, 1, -1]]

D = [[1, 1, 1, 1, -1],
     [1, -1, -1, -1, 1],
     [1, -1, -1, -1, 1],
     [1, -1, -1, -1, 1],
     [1, 1, 1, 1, -1]]

E = [[1, 1, 1, 1, 1],
     [1, -1, -1, -1, -1],
     [1, 1, 1, 1, 1],
     [1, -1, -1, -1, -1],
     [1, 1, 1, 1, 1]]

F = [[1, 1, 1, 1, 1],
     [1, -1, -1, -1, -1],
     [1, 1, 1, 1, 1],
     [1, -1, -1, -1, -1],
     [1, -1, -1, -1, -1]]

G = [[-1, 1, 1, 1, 1],
     [1, -1, -1, -1, -1],
     [1, 1, 1, 1, 1],
     [1, -1, -1, -1, 1],
     [-1, 1, 1, 1, -1]]

H = [[1, -1, -1, -1, 1],
     [1, -1, -1, -1, 1],
     [1, 1, 1, 1, 1],
     [1, -1, -1, -1, 1],
     [1, -1, -1, -1, 1]]

I = [[-1, -1, 1, -1, -1],
     [-1, -1, 1, -1, -1],
     [-1, -1, 1, -1, -1],
     [-1, -1, 1, -1, -1],
     [-1, -1, 1, -1, -1]]

J = [[1, 1, 1, 1, 1],
     [-1, -1, -1, 1, -1],
     [-1, -1, -1, 1, -1],
     [1, -1, -1, 1, -1],
     [-1, 1, 1, -1, -1]]

K = [[1, -1, -1, -1, 1],
     [1, -1, -1, 1, -1],
     [1, 1, 1, -1, -1],
     [1, -1, -1, 1, -1],
     [1, -1, -1, -1, 1]]

L = [[-1, 1, -1, -1, -1],
     [-1, 1, -1, -1, -1],
     [-1, 1, -1, -1, -1],
     [-1, 1, -1, -1, -1],
     [-1, 1, 1, 1, 1]]

M = [[1, -1, -1, -1, 1],
     [1, 1, -1, 1, 1],
     [1, -1, 1, -1, 1],
     [1, -1, -1, -1, 1],
     [1, -1, -1, -1, 1]]

N = [[1, -1, -1, -1, 1],
     [1, 1, -1, -1, 1],
     [1, -1, 1, -1, 1],
     [1, -1, -1, 1, 1],
     [1, -1, -1, -1, 1]]

O = [[-1, 1, 1, 1, -1],
     [1, -1, -1, -1, 1],
     [1, -1, -1, -1, 1],
     [1, -1, -1, -1, 1],
     [-1, 1, 1, 1, -1], ]

P = [[1, 1, 1, 1, -1],
     [1, -1, -1, -1, 1],
     [1, 1, 1, 1, -1],
     [1, -1, -1, -1, -1],
     [1, -1, -1, -1, -1]]

Q = [[-1, 1, 1, 1, -1],
     [1, -1, -1, -1, 1],
     [1, -1, 1, -1, 1],
     [1, -1, -1, 1, 1],
     [-1, 1, 1, 1, 1]]

R = [[1, 1, 1, 1, -1],
     [1, -1, -1, -1, 1],
     [1, 1, 1, 1, -1],
     [1, -1, -1, 1, -1],
     [1, -1, -1, -1, 1]]

S = [[-1, 1, 1, 1, 1],
     [1, -1, -1, -1, -1],
     [1, 1, 1, 1, -1],
     [-1, -1, -1, -1, 1],
     [1, 1, 1, 1, -1]]

T = [[1, 1, 1, 1, 1],
     [-1, -1, 1, -1, -1],
     [-1, -1, 1, -1, -1],
     [-1, -1, 1, -1, -1],
     [-1, -1, 1, -1, -1]]

U = [[1, -1, -1, -1, 1],
     [1, -1, -1, -1, 1],
     [1, -1, -1, -1, 1],
     [1, -1, -1, -1, 1],
     [-1, 1, 1, 1, -1]]

V = [[1, -1, -1, -1, 1],
     [1, -1, -1, -1, 1],
     [-1, 1, -1, 1, -1],
     [-1, 1, -1, 1, -1],
     [-1, -1, 1, -1, -1]]

W = [[1, -1, -1, -1, 1],
     [1, -1, -1, -1, 1],
     [1, -1, 1, -1, 1],
     [1, 1, -1, 1, 1],
     [1, -1, -1, -1, 1]]

X = [[1, -1, -1, -1, 1],
     [-1, 1, -1, 1, -1],
     [-1, -1, 1, -1, -1],
     [-1, 1, -1, 1, -1],
     [1, -1, -1, -1, 1]]

Y = [[1, -1, -1, -1, 1],
     [-1, 1, -1, 1, -1],
     [-1, -1, 1, -1, -1],
     [-1, -1, 1, -1, -1],
     [-1, -1, 1, -1, -1]]

Z = [[1, 1, 1, 1, 1],
     [-1, -1, -1, 1, -1],
     [-1, -1, 1, -1, -1],
     [-1, 1, -1, -1, -1],
     [1, 1, 1, 1, 1]]

letters = [A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z]


def avg_dot_vect(*vectors):
    dot = [np.dot(vectors[i], vectors[j]) for i in range(len(vectors)) for j in range(i + 1, len(vectors))]
    avg = np.mean(dot)
    return avg


def create_letter_plot(letter):
    p = sns.heatmap(letter, annot=False, cbar=False, square=True, linewidth=2, linecolor='black', cmap='Blues')
    p.xaxis.set_visible(False)
    p.yaxis.set_visible(False)
    plt.show()


def get_flatten_letter(letter):
    return np.array(letter).flatten().tolist()


def get_matrix_letter(letter):
    return [letter[0:5], letter[5:10], letter[10:15], letter[15:20], letter[20:25]]


def generate_noice(letter, probability):
    for i in range(5):
        for j in range(5):
            if random.random() < probability:
                letter[i][j] = - letter[i][j]
    return letter


def measure_orthogonality(vectors):
    orthogonality = 0
    for i in range(len(vectors)):
        for j in range(i + 1, len(vectors)):
            orthogonality += abs(np.dot(vectors[i], vectors[j]))
    return orthogonality


def find_most_orthonormal_vectors(vectors, k):
    best_subset = []
    best_subset_ortogonality = []
    best_orthogonality = float('inf')

    for subset_indices in combinations(range(len(vectors)), k):
        subset = [vectors[i] for i in subset_indices]
        orthogonality = measure_orthogonality(subset)

        if orthogonality < best_orthogonality:
            best_orthogonality = orthogonality
            best_subset.append(subset)
            best_subset_ortogonality.append(orthogonality)
            if orthogonality <= best_subset_ortogonality[0]/2:
                return best_subset, best_subset_ortogonality
    return best_subset, best_subset_ortogonality


def find_least_orthonormal_vectors(vectors, k):
    worst = None
    best_orthogonality = 0

    for subset_indices in combinations(range(len(vectors)), k):
        subset = [vectors[i] for i in subset_indices]
        orthogonality = measure_orthogonality(subset)

        if orthogonality > best_orthogonality:
            best_orthogonality = orthogonality
            worst = subset

    return worst, best_orthogonality


def get_energy(w, s):
    sum = 0
    for i in range(len(w[0])):
        for j in range(len(w)):
            sum += w[i][j] * s[i] * s[j]
    return -0.5 * sum


def energy_plot(energy):
    plt.plot(energy)
    plt.xlabel('Iteración')
    plt.ylabel('Similitud Coseno')
    plt.title('Evolución de la Similitud de Pesos con el Peso Ideal')
    plt.grid(True)
    plt.show()
