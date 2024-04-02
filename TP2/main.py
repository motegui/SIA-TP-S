from TP2.algoritmoGenetico.cruces import *
from TP2.algoritmoGenetico.seleccion import elite
from TP2.player.equipamiento import Equipamiento
from TP2.player.clase import Clase
from TP2.player.player import Player


def main():
    p1 = Player(Clase.DEFENSOR, [1.4, 150, 0, 0, 0, 0])
    p2 = Player(Clase.DEFENSOR, [1.4, 150, 0, 0, 0, 0])
    p3 = Player(Clase.DEFENSOR, [1.4, 150, 0, 0, 0, 0])
    p4 = Player(Clase.DEFENSOR, [2, 100, 20, 20, 5, 5])
    print(p1.desempeno(), p4.desempeno())
    t = elite([p1, p2, p3, p4], 10)
    for t3 in t:
        print(t3.desempeno())

if __name__ == '__main__':
    main()
