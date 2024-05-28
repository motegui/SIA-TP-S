import numpy as np

from TP4.src.hopfield import hopfield
from TP4.src.hopfieldUtils import *


def main():
    S_ESPURITO = hopfield([[1, 1, -1, -1], [-1, -1, 1, 1]], 200, [1, 1, 1, 1])
    print(S_ESPURITO)

    VR = [-1, 1, -1, -1,  -1,   -1,   1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, -1, -1, -1, -1, 1, 1, 1, 1]

    print(avg_dot_vect(Q, T, V, A))

    S, patterns = hopfield([Q, T, V, A], 500000, VR)
    print(S)
    #
    # L1 = [ 1,  1,  1,  1,  1,  1, -1, -1, -1, -1,  1, -1, -1,  1,  1,  1, -1, -1, -1,  1,  1,  1,  1,  1, 1]
    # L2 = [ 1,  1,  1,  1,  1,  1, -1, -1, -1,  1,  1, -1, -1, -1,  1,  1, -1, -1, -1,  1,  1,  1,  1,  1,1]
    # L3 = [ 1,  1,  1,  1,  1,  1, -1, -1, -1,  1 , 1 ,-1, -1 ,-1 , 1 , 1, -1, -1,  1,  1,  1,  1,  1 , 1, 1]
    # L4 = [ 1,  1,  1,  1, -1,  1, -1, -1, -1,  1,  1, -1, -1, -1,  1,  1, -1, -1, -1,  1,  1,  1,  1,  1, -1]
    #
    #
    # # print(avg_dot_vect(Q, T, V, A))
    #
    # S, patterns = hopfield([L1, L2, L3, L4], 500000, L4)
    # print(S)


if __name__ == '__main__':
    main()
