import collections
from algorithms_utils import create_path, Node


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
