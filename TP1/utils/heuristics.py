from random import random
import random

BOX = '$'


#todo: decidir si dejarla o no (es demasiado trivial)
def heuristic_non_admissible(state, goal_map):
    # Retorna un valor aleatorio como heurística
    return random.randint(0, 100)

#Heuristica NO ADMISIBLE -> en casos sobreestima
#Idea: heuristica que considera la distancia del jugador a la caja mas cercana, la distancia de esa caja a el goal mas cercano,
#luego la distancia de ese goal a la caja mas cercana, despues la distancia de esta nueva caja a otro goal mas cercano, etc
#La idea es simular el recorrido del jugador
#todo: cambiarle el nombre xd
def player_movements_heuristic(state, goal_map, player_pos):
    total_distance = 0
    box_counter = 0
    last_goal = None
    for x_pos_state in range(len(state)):
        for y_pos_state in range(len(state[0])):
            if state[x_pos_state][y_pos_state] == BOX:
                box_counter += 1
                min_distance = float('inf')
                for x_pos_goal in range(len(goal_map)):
                    for y_pos_goal in range(len(goal_map[0])):
                        if goal_map[x_pos_goal][y_pos_goal] == BOX:
                            distance = manhattan_distance(x_pos_state, y_pos_state, x_pos_goal, y_pos_goal)
                            # queremos considerar solamente el goal que esta más cerca
                            min_distance = min(min_distance, distance)
                            last_goal = [x_pos_goal, y_pos_goal]
                total_distance += min_distance
                #si es la primer caja sumamos la distancia del jugador a la caja
                #si no, hay que considerar la distancia del ultimo goal (donde "se quedo" el jugador) a la caja actual
                if box_counter == 1:
                    total_distance += manhattan_distance(x_pos_state, y_pos_state, player_pos[0], player_pos[1])
                else:
                    total_distance += manhattan_distance(x_pos_state, y_pos_state, last_goal[0], last_goal[1])

    return total_distance


def manhattan_distance(first_x_pos, first_y_post, second_x_pos, second_y_pos):
    return abs(first_x_pos - second_x_pos) + abs(first_y_post - second_y_pos)


# Idea: heuristica que considera la distancia de una caja a su goal mas cercano y la distancia del jugador
# a su caja mas cercana usando la distancia de manhattan
def manhattan_heuristic(state, goal_map, player_pos):
    total_distance = 0
    min_box_player_distance = float('inf')
    for x_pos_state in range(len(state)):
        for y_pos_state in range(len(state[0])):
            if state[x_pos_state][y_pos_state] == BOX:
                min_distance = float('inf')
                for x_pos_goal in range(len(goal_map)):
                    for y_pos_goal in range(len(goal_map[0])):
                        if goal_map[x_pos_goal][y_pos_goal] == BOX:
                            distance = manhattan_distance(x_pos_state, y_pos_state, x_pos_goal, y_pos_goal)
                            # queremos considerar solamente el goal que esta más cerca
                            min_distance = min(min_distance, distance)
                total_distance += min_distance
                box_player_distance = manhattan_distance(x_pos_state, y_pos_state, player_pos[0], player_pos[1])
                # usamos la distancia del jugador a su caja mas cercana
                min_box_player_distance = min(min_box_player_distance, box_player_distance)
    # solo lo sumamos si no terminamos
    if total_distance != 0:
        total_distance += min_box_player_distance - 1

    return total_distance


def euclidean_distance(first_x_pos, first_y_post, second_x_pos, second_y_pos):
    return ((first_x_pos - second_x_pos) ** 2 + (first_y_post - second_y_pos) ** 2) ** 0.5


def euclidean_heuristic(state, goal_map, player_pos):
    total_distance = 0
    min_box_player_distance = float('inf')
    for x_pos_state in range(len(state)):
        for y_pos_state in range(len(state[0])):
            if state[x_pos_state][y_pos_state] == BOX:
                min_distance = float('inf')
                for x_pos_goal in range(len(goal_map)):
                    for y_pos_goal in range(len(goal_map[0])):
                        if goal_map[x_pos_goal][y_pos_goal] == BOX:
                            distance = euclidean_distance(x_pos_state, y_pos_state, x_pos_goal, y_pos_goal)
                            min_distance = min(min_distance, distance)
                total_distance += min_distance
                box_player_distance = euclidean_distance(x_pos_state, y_pos_state, player_pos[0], player_pos[1])
                min_box_player_distance = min(min_box_player_distance, box_player_distance)

    if total_distance != 0:
        total_distance += min_box_player_distance - 1

    return total_distance

