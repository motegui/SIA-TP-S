import numpy as np
from matplotlib import pyplot as plt
from sklearn.metrics.pairwise import cosine_similarity


def obtained_vs_expected(weight_evol:list[list[float]], expected_weight:list[float]):
    expected_weight = np.array(expected_weight)
    similarity = []
    for weight in weight_evol:
        weight = np.array(weight)
        simil = cosine_similarity([weight], [expected_weight])[0][0]
        similarity.append(abs(simil))

    plt.plot(similarity)
    plt.xlabel('Iteración')
    plt.ylabel('Similitud Coseno')
    plt.title('Evolución de la Similitud de Pesos con el Peso Ideal')
    plt.grid(True)
    plt.show()