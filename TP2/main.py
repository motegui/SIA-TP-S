from TP2.config import config
from TP2.utils import iteracion


def main():
    rtas = iteracion(config)
    print("Generaciones: " + str(rtas[0]))
    print("Fitness promedio: " + str(rtas[2]))
    print("Mejor jugador: " + str(rtas[1]))
    print("Peor jugador: " + str(rtas[3]))


if __name__ == '__main__':
    main()