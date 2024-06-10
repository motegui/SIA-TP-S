import numpy as np

from TP5.data.font import Font3 as Font


def get_letters():
    matrix = []
    for letter in Font:
        let = []
        for line in letter:
            bin = format(line, '05b')
            bits = list(map(int, bin))
            let.append(bits)
        matrix.append(np.array(let).flatten().tolist())
    return matrix
