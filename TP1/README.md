# SIA - TP1: Métodos de Búsqueda
Grupo 4: Luciano Neimark, María Otegui, Nicolás Tordomar, Paz Aramburu
--
En este trabajo se implementó una versión simple del juego Sokoban utilizando distintos algoritmos de búsqueda:
- BFS
- DFS
- Local Greedy
- Global Greedy
- A*

A su vez, se implementaron 3 heurísticas utilizadas en los métodos de búsqueda informados:
- Player movements (no admisible)
- Manhattan entre boxes y goals (admisible)
- Euclidean entre boxes y goals (admisible)

Se encuentran distintos "levels" para probar diferentes mapas y dificultades del juego

## Requisitos
Para poder correr el proyecto se necesitan tener:
- Python3
- pip3
- pipenv

## Dependencias
El proyecto utiliza distintas dependencias. Para poder usarlo hay que insatalarlas corriendo el siguiente comando:
```shell
pipenv install
```

Ejecución
--
Para poder probar el proyecto hay que ejecutar el main.py que se encuentra en la carpeta user. En play.json se especifican las
distintas condiciones: map, algorithm y heuristic
### map
Para el mapa se debe especificar el nivel con la palabra "level" seguido de su número. Existen niveles del 1 al 8.

### algorithm
Hay 5 opcciones de algoritmos:
- BFS
- DFS
- LOCAL GREEDY
- GLOBAL GREEDY
- A*

### heuristic
Hay 4 tipos de heurísticas:
- MANHATTAN
- EUCLIDEAN
- PLAYER MOVEMENTS
- RANDOM

**En caso de usar un algoritmo no informado (BFS o DFS) se debe especificar NONE en la heurística**

Corriendo el proyecto TP1.ipynb se podrán ver todos los gráficos realizados.