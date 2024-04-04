from TP2.algoritmoGenetico.condicion_corte import contenido, estructura
from TP2.algoritmoGenetico.cruces import *
from TP2.algoritmoGenetico.seleccion import elite, universal, ruleta
from TP2.player.equipamiento import Equipamiento
from TP2.player.clase import Clase
from TP2.player.player import Player
from TP2.config import config

PROBABILIDAD_MUTACION = config.get('probabilidad_mutacion')
def main():

    #armar la pobla inicial. agarro el numerito y creo tipitos (del tipo)
    #arrancamos la iter

    #while (condicion de corte not true):
        #de la poblacion vemos cual es K (sacado del json)
        #Seleccionas los k padres ( metodo de seleccccc 1 y 2 viendo la formulita y el porcentaje A que lo sacas del json)
        #Armas K hijos (metodos para cruzar que sacas de json) llamando a la funcion que este en cruces.
        #Mutacion time (agarro el METODO DE MUTE (SON 3), prob inicial y uniforme o no uniforme! si no es uniforme la funcion....... y el factor)
        #De la nueva poblacion (k + n) agarro con el metodo de selcccc vol 2 los n muchachos (joven o tradicional SE SACA DEL JSON Y B Y METODO 3 y 4 tambien)
        #REPITO TOD



    aux = [1, 2, 3, 4, 5, 1, 1, 1]
    aux.remove(1)
    print(aux)
    print(2 in aux)



    p1 = Player(Clase.DEFENSOR, [1.4, 20, 20, 20, 20, 70])
    p2 = Player(Clase.DEFENSOR, [1.4, 70, 20, 20, 20, 20])
    p3 = Player(Clase.DEFENSOR, [1.4, 10, 10, 10, 20, 100])
    p4 = Player(Clase.DEFENSOR, [2, 100, 500, 220, 5000, 5])
    print(p4.cromosoma)
    print(PROBABILIDAD_MUTACION)
    poblacion = [p1, p2, p3, p4]
    t = universal([p1, p2, p3, p4], 10)
    for j, t3 in enumerate(t):
        a = ruleta(poblacion, 200)
        usar = estructura(poblacion, j)

        print(usar)



if __name__ == '__main__':
    main()
