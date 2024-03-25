from random import random
import random

BOX = '$'


# todo: decidir si dejarla o no (es demasiado trivial)
def heuristic_non_admissible(state, goal_map):
    # Retorna un valor aleatorio como heurística
    return random.randint(0, 100)


# Heuristica NO ADMISIBLE -> en casos sobreestima
# Idea: heuristica que considera la distancia del jugador a la caja mas cercana, la distancia de esa caja a el goal mas cercano,
# luego la distancia de ese goal a la caja mas cercana, despues la distancia de esta nueva caja a otro goal mas cercano, etc
# La idea es simular el recorrido del jugador
# todo: cambiarle el nombre xd
def player_movements_heuristic(current_node):
    total_distance = 0
    min_box_player_distance = float('inf')
    last_goal = None
    for box in current_node.state.boxes:
        box_player_distance = manhattan_distance(box, current_node.position)
        min_box_player_distance = min(min_box_player_distance, box_player_distance)
        min_box_goal_distance = float('inf')
        for goal in current_node.state.goals:
            box_goal_distance = manhattan_distance(box, goal)
            # queremos considerar solamente el goal que esta más cerca
            if min_box_goal_distance > box_goal_distance:
                last_goal = goal
                min_box_goal_distance = box_goal_distance
        total_distance += min_box_goal_distance
        # si es la primer caja (last_goal == None) sumamos la distancia del jugador a la caja
        # si no, hay que considerar la distancia del ultimo goal (donde "se quedo" el jugador) a la caja actual
        if last_goal is None:
            total_distance += manhattan_distance(box, current_node.position)
        else:
            total_distance += manhattan_distance(box, last_goal)
    return total_distance


def manhattan_distance(first, second):
    return abs(first[0] - second[0]) + abs(first[1] - second[1])


# Idea: heuristica que considera la distancia de una caja a su goal mas cercano y la distancia del jugador
# a su caja mas cercana usando la distancia de manhattan
def manhattan_heuristic(current_node):
    total_distance = 0
    min_box_player_distance = float('inf')
    closest_box_to_goal = None
    for box in current_node.state.boxes:
        box_player_distance = manhattan_distance(box, current_node.position)
        min_box_player_distance = min(min_box_player_distance, box_player_distance)
        if box not in current_node.state.goals:
            min_box_goal_distance = float('inf')
            for goal in current_node.state.goals:
                #solo comparo aquellos que no estan "usados"
                if goal not in current_node.state.boxes:
                    box_goal_distance = manhattan_distance(box, goal)
                    min_box_goal_distance = min(min_box_goal_distance, box_goal_distance)
            # if min_box_goal_distance < min_boxes_distance:
            #     closest_box_to_goal = box
            #     min_boxes_distance = min_box_goal_distance
            total_distance += min_box_goal_distance
    #probando de sumar la distancia del jugador a la caja que esta mas cerca de un goal
    if total_distance != 0:
        total_distance += min_box_player_distance #si sumamos esto tarda mas todo
    return total_distance


def euclidean_distance(first, second):
    return ((first[0] - second[0]) ** 2 + (first[1] - second[1]) ** 2) ** 0.5


def euclidean_heuristic(current_node):
    total_distance = 0
    min_box_player_distance = float('inf')
    for box in current_node.state.boxes:
        box_player_distance = euclidean_distance(box, current_node.position)
        min_box_player_distance = min(min_box_player_distance, box_player_distance)
        min_box_goal_distance = float('inf')
        for goal in current_node.state.goals:
            box_goal_distance = euclidean_distance(box, goal)
            min_box_goal_distance = min(min_box_goal_distance, box_goal_distance)
        total_distance += min_box_goal_distance
    if total_distance != 0:
        total_distance += min_box_player_distance - 1
    return total_distance
