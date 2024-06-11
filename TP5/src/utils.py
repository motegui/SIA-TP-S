import numpy as np

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
    return matrix


def test_network(letters, network):
    labels = ["`", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
              "t", "u", "v", "w", "x", "y", "z", "{", "|", "}", "~", "DEL"]
    for j, letter in enumerate(letters):
        l = network.forward_propagation(letter)
        l = [let.round().astype(int) for let in l]
        let_error = 0
        for i in range(0, len(letter)):
            if letter[i] != l[i]:
                let_error += 1
        print(f'Letter {labels[j]}, error {let_error} \n')
