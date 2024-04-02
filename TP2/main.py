from TP2.algoritmoGenetico.condicion_corte import contenido, estructura
from TP2.algoritmoGenetico.cruces import *
from TP2.algoritmoGenetico.seleccion import elite, universal, ruleta
from TP2.player.equipamiento import Equipamiento
from TP2.player.clase import Clase
from TP2.player.player import Player


def main():
    # aux = [1, 2, 3, 4, 5, 1, 1, 1]
    # aux.remove(1)
    # print(aux)
    # print(2 in aux)

    p1 = Player(Clase.DEFENSOR, [1.4, 20, 20, 20, 20, 70])
    p2 = Player(Clase.DEFENSOR, [1.4, 70, 20, 20, 20, 20])
    p3 = Player(Clase.DEFENSOR, [1.4, 10, 10, 10, 20, 100])
    p4 = Player(Clase.DEFENSOR, [2, 100, 500, 220, 5000, 5])
    print(p4.cromosoma)
    poblacion = [p1, p2, p3, p4]
    t = universal([p1, p2, p3, p4], 10)
    for j, t3 in enumerate(t):
        a = ruleta(poblacion, 200)
        usar = estructura(poblacion, j)

        print(usar)



if __name__ == '__main__':
    main()
