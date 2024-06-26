import random
import numpy as np
from matplotlib import pyplot as plt
from TP5.data.font import Font3 as Font


def get_letters():
    matrix = []
    for letter in Font:
        let = []
        for line in letter:
            bin = format(line, '05b')
            bits = list(map(int, bin))
            # bits = [-1 if x == 0 else x for x in bits]
            let.append(bits)
        matrix.append(np.array(let).flatten().tolist())
    print(matrix)
    return matrix


def test_network(input_data, output_data, network, print_errors=True):
    labels = get_labels_by_letters(output_data)
    forward = []
    errors = []
    for j, letter in enumerate(input_data):
        l = network.forward_propagation(letter)
        l = [1 if let >= 0 else 0 for let in l]
        forward.append(l)
        let_error = 0
        for i in range(0, len(letter)):
            if output_data[j][i] != l[i]:
                let_error += 1
        if print_errors:
            print(f'Letter {labels[j]}, error {let_error} \n')
        errors.append(let_error)

    return forward, input_data, output_data, errors


def get_letters_map():
    labels = ["`", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
              "t", "u", "v", "w", "x", "y", "z", "{", "|", "}", "~", "DEL"]

    letters = [
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1],
        [0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0],
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0],
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0],
        [0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0],
        [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1],
        [0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0],
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
        [0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0],
        [0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

    map = {}

    for i in range(len(letters)):
        map[tuple(letters[i])] = labels[i]

    return map


def get_labels_by_letters(letters):
    labels = []
    map = get_letters_map()
    for letter in letters:
        label = map[tuple(letter)]
        labels.append(label)

    return labels


def plot_progress(l1, l2, encoder, decoder):
    p1 = encoder.forward_propagation(l1)
    p2 = encoder.forward_propagation(l2)

    points = generar_puntos_entre(p1, p2, 14)
    letters = [l1]
    for point in points:
        letter = decoder.forward_propagation([point[0], point[1]])
        letter = cast_letter(letter)
        letters.append(letter)
    letters.append(l2)

    plot_letters(letters)


def plot_letters(letters, row=4, col=4):
    plt.clf()
    fig, axs = plt.subplots(row, col)

    # Mostrar los gráficos

    for i, ax in enumerate(axs.flat):
        if i == len(letters): break
        matriz = np.array(letters[i]).reshape(7, 5)
        # Graficar la matriz sin escalas ni números de ejes
        ax.imshow(matriz, cmap='nipy_spectral_r', interpolation='nearest')

        # Ocultar los ejes
        ax.axis('off')

        # Mostrar la trama

    # Ajustar el espaciado entre los subplots
    plt.tight_layout()
    plt.show()


def cast_letter(letter):
    return [0 if let <= 0 else 1 for let in letter]


def generar_puntos_entre(coordenada1, coordenada2, cantidad=10):
    x1, y1 = coordenada1
    x2, y2 = coordenada2

    # Calcular las diferencias en x y y
    delta_x = (x2 - x1) / (cantidad - 1)
    delta_y = (y2 - y1) / (cantidad - 1)

    # Generar los puntos intermedios
    puntos = [(x1 + i * delta_x, y1 + i * delta_y) for i in range(cantidad)]

    return puntos


def noise_letters(letters, cant, noise_proportion):
    noisy = []
    clean = []
    # Number of elements to modify
    num_noise_elements = int(noise_proportion * 35)
    for letter in letters:
        for i in range(cant):
            clean.append(letter)
            # Generate random positions for the noise
            noise_positions = np.random.choice(35, num_noise_elements, replace=False)

            # Apply "salt and pepper" noise
            noisy_array = letter.copy()
            for pos in noise_positions:
                noisy_array[pos] = 1 - noisy_array[pos]

            noisy.append(noisy_array)

    return noisy, clean


def remove_part(letters, cant):
    removed_letters = []
    clean_letters = []
    for letter in letters:
        for i in range(cant):
            clean_letters.append(letter)
            matriz = np.array(letter).reshape((7, 5))

            # Seleccionar un elemento aleatorio

            fila_random = random.randint(0, 6)
            col_random = random.randint(0, 4)
            while matriz[fila_random][col_random] == 0:
                fila_random = random.randint(0, 6)
                col_random = random.randint(0, 4)

            # Crear una lista de posiciones vecinas (incluyendo diagonales)
            vecinos = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

            # Convertir el elemento aleatorio y sus vecinos en 0
            for dr, dc in vecinos + [(0, 0)]:
                fila = fila_random + dr
                col = col_random + dc
                if 0 <= fila < 7 and 0 <= col < 5:
                    matriz[fila, col] = 0

            # Convertir la matriz de vuelta en un array de 35 elementos
            removed_letters.append(matriz.flatten().tolist())

    return removed_letters, clean_letters


def test_emoji_network(input_data, output_data, network, print_errors=True):
    labels = ['carita feliz', 'carita triste', 'carita aburrida', 'carita sorprendida', 'flecha arriba', 'flecha abajo',
              'cruz', 'tick']
    forward = []
    errors = []
    for j, letter in enumerate(input_data):
        l = network.forward_propagation(letter)
        l = [1 if let >= 0 else 0 for let in l]
        forward.append(l)
        let_error = 0
        for i in range(0, len(letter)):
            if output_data[j][i] != l[i]:
                let_error += 1
        if print_errors:
            print(f'Letter {labels[j]}, error {let_error} \n')
        errors.append(let_error)

    return forward, input_data, output_data, errors


def plot_emoji_progress(l1, l2, encoder, decoder):
    emojis = []
    grid_x = np.linspace(l1, l2, 15)
    grid_y = np.linspace(l1, l2, 15)[::-1]
    for i, yi in enumerate(grid_y):
        for j, xi in enumerate(grid_x):
            emoji = decoder.forward_propagation([yi, xi])
            emojis.append(emoji)

    plot_emojis(emojis)


def plot_emojis(emojis):
    plt.clf()
    fig, axs = plt.subplots(15, 15, figsize=(10, 10))
    fig.patch.set_facecolor('black')

    # Mostrar los gráficos

    for i, ax in enumerate(axs.flat):
        if i == len(emojis): break
        matriz = np.array(emojis[i]).reshape(8, 8)
        ax.imshow(matriz, cmap='Greys_r', interpolation='nearest')
        ax.axis('off')
        ax.set_facecolor('black')  # Cambiar el color de fondo de los ejes a negro
    plt.subplots_adjust(wspace=0.5, hspace=0.5)
    plt.show()
