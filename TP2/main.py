import math

from TP2.algoritmoGenetico.condicion_corte import contenido, estructura, optimo, cantidad_generaciones
from TP2.algoritmoGenetico.cruces import *
from TP2.algoritmoGenetico.no_uniformes import creciente, decreciente
from TP2.algoritmoGenetico.seleccion import elite, universal, ruleta
from TP2.player.clase import Clase
from TP2.player.player import Player
from TP2.config import config
from TP2.player.player import generar_cromosoma
from TP2.algoritmoGenetico.mutacion import mutar_poblacion, gen

PROBABILIDAD_MUTACION = config.get('probabilidad_mutacion')


condiciones_corte = {
    'estructura': estructura,
    'optimo': optimo,
    'contenido': contenido,
    'cantidad_gen': cantidad_generaciones
}

metodos_seleccion = {
    'elite': elite,
    'universal': universal,
    'ruleta': ruleta
}

metodo_cruce = {
    'un_punto': un_punto,
    'dos_puntos': dos_puntos
}

metodos_no_uniformes = {
    "creciente": creciente,
    "decreciente": decreciente
}


def main():
    clase = config.get("clase")
    n = config.get('n')

    poblacion_inicial = []
    for i in range(0, n):
        cromosoma = generar_cromosoma()
        poblacion_inicial.append(Player(Clase[clase], cromosoma))

    poblacion_actual = poblacion_inicial
    generacion_actual = 1
    while not condiciones_corte[config.get('condicion_corte').get('tipo')](poblacion_actual, generacion_actual):
        K = config.get("K")
        A = config.get("A")
        B = config.get("B")

        padres = (metodos_seleccion[config.get('metodo1')](poblacion=poblacion_actual, n=math.floor(K * A), generacion=generacion_actual) +
                  metodos_seleccion[config.get('metodo2')](poblacion=poblacion_actual, n=K - math.floor(K * A), generacion=generacion_actual))

        cromosomas_hijos = cruzar_poblacion(padres, metodo_cruce[config.get('metodo_cruce')])

        prob_mutacion = config.get('probabilidad_mutacion')
        if config.get('funcion_no_uniforme') is not None:
            prob_mutacion = (metodos_no_uniformes[config.get('funcion_no_uniforme')]
                             (prob_mutacion,
                              generacion_actual, config.get('factor')
                              ))

        cromosomas_mutados = mutar_poblacion(cromosomas_hijos, gen, prob_mutacion)

        hijos = []
        for cromosoma in cromosomas_mutados:
            hijos.append(Player(Clase[clase], cromosoma))

        if not config.get('favorecer_jovenes'):
            poblacion_k_mas_n = poblacion_actual + hijos
            poblacion_actual = (
                    metodos_seleccion[config.get('metodo3')](poblacion=poblacion_k_mas_n, n=math.floor(n * B), generacion=generacion_actual)
                    + metodos_seleccion[config.get('metodo4')](poblacion=poblacion_k_mas_n, n=n - math.floor(n * B), generacion=generacion_actual))
        else:
            if K >= n:
                poblacion_actual = (
                        metodos_seleccion[config.get('metodo3')](poblacion=hijos, size=math.floor(n * B))
                        + metodos_seleccion[config.get('metodo4')](poblacion=hijos,
                                                                   n=n - math.floor(n * B),
                                                                   generacion=generacion_actual))
            else:
                poblacion_actual = hijos + (
                        metodos_seleccion[config.get('metodo3')](poblacion=poblacion_actual,
                                                                 n=math.floor((n - K) * B),
                                                                 generacion=generacion_actual)
                        + metodos_seleccion[config.get('metodo4')](poblacion=poblacion_actual,
                                                                   n=(n - K) - math.floor((n - K) * B),
                                                                   generacion=generacion_actual))
        generacion_actual += 1
    print(poblacion_actual)


if __name__ == '__main__':
    main()
