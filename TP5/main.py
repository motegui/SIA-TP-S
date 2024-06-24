import numpy as np
from TP4.src.hopfieldUtils import find_most_orthonormal_vectors
from TP5.src.autoencoder import autoencoder, plot_latent_space
from TP5.src.utils import get_letters, test_network, plot_letters, noise_letters, remove_part, plot_progress


def pixel_error(output, expected):
    error = 0
    for i in range(len(output)):
        if output[i] > 0:
            if expected[i] != 1:
                error += 1
        else:
            if expected[i] != -1:
                error += 1
    return error


def ej1():
    letters_pattern = get_letters()
    network = autoencoder(letters_pattern, letters_pattern)
    encoder, decoder = network.get_decoder_encoder()
    plot_latent_space(letters_pattern, letters_pattern, encoder)
    test_network(letters_pattern, letters_pattern, network)

    l1 = letters_pattern[1]
    l2 = letters_pattern[2]

    plot_progress(l1, l2, encoder, decoder)

    l1 = letters_pattern[3]
    l2 = letters_pattern[10]
    plot_progress(l1, l2, encoder, decoder)


def ej2():
    letters_pattern = get_letters()[2:20]
    letters_pattern = find_most_orthonormal_vectors(letters_pattern, 6)[0][-1]
    letters0 = noise_letters(letters_pattern, 1, 0.15)
    letters1 = noise_letters(letters_pattern, 1, 0.2)
    letters2 = noise_letters(letters_pattern, 1, 0.25)
    letters = letters0[0] + letters1[0] + letters2[0]
    letters_clean = letters0[1] + letters1[1] + letters2[1]
    network = autoencoder(letters, letters_clean)
    for i in np.arange(0, 1, 0.05):
        out, noisy, clean, error = test_network(noise_letters(letters_pattern, 1, i)[0], letters_pattern, network,
                                                print_errors=False)
        plotted = []
        for o, n, c in zip(out[:6], noisy[:6], clean[:6]):
            plotted.append(n)
            plotted.append(o)
            plotted.append(c)
        plot_letters(plotted, 4, 3)
        mean = np.mean(error)
        print(f'mean ERROR: {mean}')


def removed_part():
    letters_pattern = get_letters()
    print('im out!')
    letters = remove_part(letters_pattern, 3)
    network = autoencoder(letters[0], letters[1])
    encoder, decoder = network.get_decoder_encoder()
    plot_latent_space(letters_pattern, remove_part(letters_pattern, 1)[0], encoder)
    out, noisy, clean, e = test_network(remove_part(letters_pattern, 1)[0], letters_pattern, network)
    for o, n, c in zip(out[:5], noisy[:5], clean[:5]):
        plot_letters([n, o, c], 1, 3)


def main():
    ej1()
    ej2()
    removed_part()


if __name__ == '__main__':
    main()
