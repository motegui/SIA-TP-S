from TP4.src.hopfield import hopfield


def main():
    # S_ESPURITO = hopfield([[1, 1, -1, -1], [-1, -1, 1, 1]], 200, [1, 1, 1, 1])
    # print(S_ESPURITO)

    S = hopfield([[1, 1, -1, -1], [-1, -1, 1, 1]], 200, [1, -1, -1, -1])
    print(S)


if __name__ == '__main__':
    main()
