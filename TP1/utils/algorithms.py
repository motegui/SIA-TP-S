import collections


class Node:
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def bfs(maze, start_position, end_position, generate_children):
    initial_node = Node(None, start_position)
    end_node = Node(None, end_position)
    closed_list = []
    opened_list = collections.deque([initial_node])
    closed_list.append(initial_node)

    while opened_list:
        current_node = opened_list.popleft()
        if current_node.position == end_node.position:
            return create_path(initial_node, current_node)

        # Llamar a generate children aca porque no los tenes de entrada...
        for child in generate_children(current_node, maze):
            if child not in closed_list:
                closed_list.append(child)
                opened_list.append(child)


def dfs(maze, start_position, end_position, generate_children):
    initial_node = Node(None, start_position)
    end_node = Node(None, end_position)
    closed_list = [initial_node]
    opened_list = collections.deque([initial_node])

    while opened_list:
        current_node = opened_list.pop()
        if current_node.position == end_node.position:
            return create_path(initial_node, current_node)

        # Llamar a generate children aca porque no los tenes de entrada...
        for child in generate_children(current_node, maze):
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
def astar(maze, start_position, end_position, generate_children, heuristic):
    initial_node = Node(None, start_position)
    initial_node.h = initial_node.g = initial_node.f = 0

    end_node = Node(None, end_position)
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

        if current_node.position == end_node.position:
            return create_path(initial_node, current_node)

        # Generar los nodos hijos y agregar
        children = generate_children(current_node, maze)

        for child in children:
            if child in closed_list:
                continue

            child.g = current_node.g + 1  # distancia hasta aca + distancia de ir de current a child (entiendo que es
            # 1 porque es 1 movimiento...)
            child.h = heuristic(child.position, end_position)
            child.f = child.g + child.h

            is_open = False
            for openNode in opened_list:
                if child.position == openNode.position and child.g > openNode.g:
                    is_open = True

            if is_open:
                continue
            opened_list.append(child)


def euclidean_heuristic(position, end_position):
    return ((position[0] - end_position[0]) ** 2) + ((position[1] - end_position[1]) ** 2)


def manhattan_distance(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])


def generate_children_maze(current_node, maze):
    children = []
    for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:  # Adjacent squares

        # Get node position
        node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

        # Make sure within range
        if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (
                len(maze[len(maze) - 1]) - 1) or node_position[1] < 0:
            continue

        # Make sure walkable terrain
        if maze[node_position[0]][node_position[1]] != 0:
            continue

        # Create new node
        new_node = Node(current_node, node_position)

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

    start = (0, 0)
    end = (7, 10)

    path = astar(maze, start, end, generate_children_maze, euclidean_heuristic)
    print(path)


# [(0, 0), (1, 1), (2, 2), (3, 3), (4, 3), (5, 3), (6, 4), (7, 5), (7, 6)]
# [(0, 0), (1, 1), (2, 2), (3, 3), (4, 3), (5, 3), (6, 4), (7, 5), (7, 6)]
if __name__ == '__main__':
    main()
