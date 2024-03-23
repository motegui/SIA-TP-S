import collections
from copy import copy, deepcopy

WALL = '#'
BOX = '$'
EMPTY = ' '


def IS_SOLID(x):
    return x == '#' or x == '$'


class Node:
    def __init__(self, parent=None, position=None, state=None):
        self.parent = parent
        self.position = position
        self.state = state

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return all([a == b for a, b in zip(self.state, other.state)]) and self.position == other.position

    def map_equals(self, other):
        return all([a == b for a, b in zip(self.state, other.state)])


def bfs(map, start_position, goal_map, generate_children, heuristic):
    initial_node = Node(None, start_position, map)
    end_node = Node(None, None, goal_map)
    end_node.h = end_node.g = end_node.f = 0
    closed_list = []
    opened_list = collections.deque([initial_node])
    closed_list.append(initial_node)

    while opened_list:
        current_node = opened_list.popleft()
        if current_node.map_equals(end_node):
            return create_path(initial_node, current_node)

        # Llamar a generate children aca porque no los tenes de entrada...
        for child in generate_children(current_node):
            if child not in closed_list:
                closed_list.append(child)
                opened_list.append(child)


# BUG
def dfs(map, start_position, goal_map, generate_children, heuristic):
    initial_node = Node(None, start_position, map)
    end_node = Node(None, None, goal_map)
    end_node.h = end_node.g = end_node.f = 0
    closed_list = [initial_node]
    opened_list = collections.deque([initial_node])

    while opened_list:
        current_node = opened_list.pop()
        if current_node.map_equals(end_node):
            return create_path(initial_node, current_node)

        # Llamar a generate children aca porque no los tenes de entrada...
        for child in generate_children(current_node):
            if child not in closed_list:
                closed_list.append(child)
                opened_list.append(child)


def local_greedy(maze, start_position, end_position, generate_children, heuristic):
    closed_list = []

    initial_node = Node(None, start_position)
    initial_node.h = initial_node.g = initial_node.f = 0

    end_node = Node(None, end_position)
    end_node.h = end_node.g = end_node.f = 0

    opened_list = collections.deque([initial_node])
    closed_list.append(initial_node)

    while opened_list:
        current_node = opened_list.pop()

        if current_node.position == end_node.position:
            return create_path(initial_node, current_node)

        ordered_children = sorted(generate_children(current_node, maze), key=lambda x: x.h, reverse=True)
        # Llamar a generate children aca porque no los tenes de entrada...
        for child in ordered_children:
            child.g = current_node.g + 1  # distancia hasta aca + distancia de ir de current a child
            child.h = heuristic(child.position, end_position)
            child.f = child.g + child.h

            if child not in closed_list:
                closed_list.append(child)
                opened_list.append(child)


def global_greedy(maze, start_position, end_position, generate_children, heuristic):
    closed_list = []

    initial_node = Node(None, start_position)
    initial_node.h = initial_node.g = initial_node.f = 0

    end_node = Node(None, end_position)
    end_node.h = end_node.g = end_node.f = 0

    opened_list = collections.deque([initial_node])
    closed_list.append(initial_node)

    while opened_list:
        current_node = opened_list.pop()

        if current_node.position == end_node.position:
            return create_path(initial_node, current_node)

        children = generate_children(current_node, maze)
        # Llamar a generate children aca porque no los tenes de entrada...
        for child in children:
            child.g = current_node.g + 1  # distancia hasta aca + distancia de ir de current a child
            # (entiendo que es 1 porque es 1 movimiento...)
            child.h = heuristic(child.position, end_position)
            child.f = child.g + child.h

            if child not in closed_list:
                closed_list.append(child)
                opened_list.append(child)

        opened_list = collections.deque(sorted(opened_list, key=lambda x: x.h, reverse=True))


# Para saber que nodo expandir, calcula la euristica
# en vez de queue.pop, busco el mejor.

# Generate children devuelve un array de hijos dado el nodo. (movimientos posibles desde un tablero)
# Generate children devuelve un array de hijos dado el nodo. (movimientos posibles desde un tablero)
def astar(map, start_position, goal_map, generate_children, heuristic):
    initial_node = Node(None, start_position, map)
    initial_node.h = heuristic(map, goal_map)
    initial_node.g = 0
    initial_node.f = initial_node.h

    end_node = Node(None, None, goal_map)
    end_node.h = end_node.g = end_node.f = 0

    opened_list = [initial_node]
    closed_list = []

    while opened_list:

        current_node = opened_list[0]
        current_index = 0
        # Calculo el nodo de menor f. (f = g + h)
        for (i, node) in enumerate(opened_list):
            if node.f == current_node.f and node.h < current_node.h:
                current_node = node
                current_index = i
            elif node.f < current_node.f:
                current_node = node
                current_index = i

        opened_list.pop(current_index)
        closed_list.append(current_node)
        print(current_node.state)
        print("\n")
        if current_node.map_equals(end_node):
            return create_path(initial_node, current_node)

        # Generar los nodos hijos y agregar
        children = generate_children(current_node)

        for child in children:
            if child in closed_list:
                continue

            child.g = current_node.g + 1  # distancia hasta aca + distancia de ir de current a child (entiendo que es
            # 1 porque es 1 movimiento...)
            child.h = heuristic(child.state, goal_map)
            child.f = child.g + child.h

            is_open = False
            for openNode in opened_list:
                if child == openNode and child.g > openNode.g:
                    is_open = True

            if is_open:
                continue
            opened_list.append(child)


def euclidean_heuristic(state, goal_map):
    total_distance = 0
    for x_pos_state in range(len(state)):
        for y_pos_state in range(len(state[0])):
            if state[x_pos_state][y_pos_state] == BOX:
                min_distance = float('inf')
                for x_pos_goal in range(len(goal_map)):
                    for y_pos_goal in range(len(goal_map[0])):
                        if goal_map[x_pos_goal][y_pos_goal] == '$':
                            distance = (x_pos_state - x_pos_goal) ** 2 + (y_pos_state - y_pos_goal) ** 2
                            min_distance = min(min_distance, distance)
                total_distance += min_distance

    return total_distance
    # return ((position[0] - end_position[0]) ** 2) + ((position[1] - end_position[1]) ** 2)


def manhattan_heuristic(state, goal_map):
    total_distance = 0

    for x_pos_state in range(len(state)):
        for y_pos_state in range(len(state[0])):
            if state[x_pos_state][y_pos_state] == BOX:
                min_distance = float('inf')
                for x_pos_goal in range(len(goal_map)):
                    for y_pos_goal in range(len(goal_map[0])):
                        if goal_map[x_pos_goal][y_pos_goal] == '$':
                            distance = abs(x_pos_state - x_pos_goal) + abs(y_pos_state - y_pos_goal)
                            min_distance = min(min_distance, distance)
                total_distance += min_distance

    return total_distance


def generate_new_state(current_node, new_position):
    new_map = deepcopy(current_node.state)
    new_map[current_node.position[0]][current_node.position[1]] = EMPTY

    if new_map[current_node.position[0] + new_position[0]][current_node.position[1] + new_position[1]] == BOX:
        new_map[current_node.position[0] + new_position[0]][current_node.position[1] + new_position[1]] = EMPTY
        new_box_position = (
            current_node.position[0] + 2 * new_position[0], current_node.position[1] + 2 * new_position[1])
        new_map[new_box_position[0]][new_box_position[1]] = BOX
    return new_map


def generate_children_maze(current_node):
    children = []
    for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:  # Adjacent squares
        # Get node position
        node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

        # Make sure walkable terrain
        if current_node.state[node_position[0]][node_position[1]] == WALL:
            continue
        if current_node.state[node_position[0]][node_position[1]] == BOX:
            new_box_position = (node_position[0] + new_position[0], node_position[1] + new_position[1])
            if IS_SOLID(current_node.state[new_box_position[0]][new_box_position[1]]):
                continue

        new_state = generate_new_state(current_node, new_position)

        # Create new node
        new_node = Node(current_node, node_position, new_state)

        # Append
        children.append(new_node)

    return children


def create_path(initial_node, current_node):
    path = [current_node.position]
    while current_node.position != initial_node.position:
        current_node = current_node.parent
        path.append(current_node.position)
    return path[::-1]  # Doy vuelta asi arranca por el nodo inicial.


def main():
    maze = [[0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0]]
    sokoban_map = [
        [' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', '#', '#', '#', '#', '#', ' ', '#', '#', '#', '#', '#', ' ', ' '],
        [' ', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', ' '],
        ['#', '#', ' ', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', ' ', '#', '#'],
        ['#', ' ', ' ', '#', '#', ' ', ' ', ' ', ' ', ' ', '#', '#', ' ', ' ', '#'],
        ['#', ' ', '#', '#', ' ', ' ', '#', ' ', '#', ' ', ' ', '#', '#', ' ', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', '$', ' ', '$', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', '#', '#', '#', ' ', ' ', '#', '#', '#', ' ', ' ', '#', '#', '#', '#'],
        [' ', ' ', ' ', '#', '#', '#', '#', ' ', '#', '#', '#', '#', ' ', ' ', ' ']
    ]

    sokoban_easy_map = [
        [' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', '#', '$', '#', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', '#', '#', '#', '#', '#', ' ', '#', '#', '#', '#', '#', ' ', ' '],
        [' ', '#', '#', ' ', ' ', ' ', ' ', '$', ' ', ' ', ' ', ' ', '#', '#', ' '],
        ['#', '#', ' ', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', ' ', '#', '#'],
        ['#', ' ', ' ', '#', '#', ' ', ' ', ' ', ' ', ' ', '#', '#', ' ', ' ', '#'],
        ['#', ' ', '#', '#', ' ', ' ', '#', ' ', '#', ' ', ' ', '#', '#', ' ', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', '#', '#', '#', ' ', ' ', '#', '#', '#', ' ', ' ', '#', '#', '#', '#'],
        [' ', ' ', ' ', '#', '#', '#', '#', ' ', '#', '#', '#', '#', ' ', ' ', ' ']
    ]

    sokoban_medium_map = [
        [' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', '#', '#', '#', '#', '#', ' ', '#', '#', '#', '#', '#', ' ', ' '],
        [' ', '#', '#', ' ', ' ', '$', ' ', ' ', ' ', '$', ' ', ' ', '#', '#', ' '],
        ['#', '#', ' ', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', ' ', '#', '#'],
        ['#', ' ', ' ', '#', '#', ' ', ' ', ' ', ' ', ' ', '#', '#', ' ', ' ', '#'],
        ['#', ' ', '#', '#', ' ', ' ', '#', ' ', '#', ' ', ' ', '#', '#', ' ', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', '#', '#', '#', ' ', ' ', '#', '#', '#', ' ', ' ', '#', '#', '#', '#'],
        [' ', ' ', ' ', '#', '#', '#', '#', ' ', '#', '#', '#', '#', ' ', ' ', ' ']
    ]

    sokoban_goal = [
        [' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', '#', '$', '#', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', '#', '#', '#', '#', '#', '$', '#', '#', '#', '#', '#', ' ', ' '],
        [' ', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', ' '],
        ['#', '#', ' ', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', ' ', '#', '#'],
        ['#', ' ', ' ', '#', '#', ' ', ' ', ' ', ' ', ' ', '#', '#', ' ', ' ', '#'],
        ['#', ' ', '#', '#', ' ', ' ', '#', ' ', '#', ' ', ' ', '#', '#', ' ', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', '#', '#', '#', ' ', ' ', '#', '#', '#', ' ', ' ', '#', '#', '#', '#'],
        [' ', ' ', ' ', '#', '#', '#', '#', ' ', '#', '#', '#', '#', ' ', ' ', ' ']
    ]
    start = (7, 7)

    path = astar(sokoban_medium_map, start, sokoban_goal, generate_children_maze, manhattan_heuristic)
    print(path)


# [(0, 0), (1, 1), (2, 2), (3, 3), (4, 3), (5, 3), (6, 4), (7, 5), (7, 6)]
# [(0, 0), (1, 1), (2, 2), (3, 3), (4, 3), (5, 3), (6, 4), (7, 5), (7, 6)]


if __name__ == '__main__':
    main()
