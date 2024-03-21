import collections


def bfs(graph, root):
    visited = set()
    queue = collections.deque([root])
    visited.add(root)
    print("root: " + str(root))

    while queue:
        vertex = queue.popleft()
        print("node: " + str(vertex))

        # Llamar a generate children aca porque no los tenes de entrada...
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


def dfs(graph, root):
    visited = set()
    queue = collections.deque([root])
    visited.add(root)
    print("root: " + str(root))

    while queue:
        vertex = queue.pop()
        print("node: " + str(vertex))

        # Llamar a generate children aca porque no los tenes de entrada...
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


class Node():
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

def local_greedy(maze, startPosition, endPosition, generateChildren, heuristic):

    initialNode = Node(None, startPosition)
    initialNode.h = initialNode.g = initialNode.f = 0

    endNode = Node(None, endPosition)
    endNode.h = endNode.g = endNode.f = 0

    openList = [initialNode]
    closedList = []

    while openList:
        currentNode = openList.pop(0)
        closedList.append(currentNode)

        if currentNode == endNode:
            path = [currentNode.position]
            while currentNode != initialNode:
                currentNode = currentNode.parent
                path.append(currentNode.position)
            return path[::-1]  # Doy vuelta asi arranca por el nodo inicial.

        # Generar los nodos hijos y agregar
        children = generateChildren(currentNode, maze)

        lowestHChild = None
        lowestH = float('inf')

        for child in children:

            isClosed = False
            for closedChild in closedList:
                if closedChild == child:
                    isClosed = True

            if isClosed:
                continue

            if child not in closedList:
                child.g = currentNode.g + 1  # distancia hasta aca + distancia de ir de current a child (entiendo que es 1 porque es 1 movimiento...)
                child.h = heuristic(child.position, endPosition)
                child.f = child.g + child.h

            if child.h < lowestH:
                lowestHChild = child
                lowestH = child.h

        if lowestHChild:
            openList.append(lowestHChild)

# Para saber que nodo expandir, calcula la euristica
# en vez de queue.pop, busco el mejor.

# Generate children devuelve un array de hijos dado el nodo. (movimientos posibles desde un tablero)
def astar(maze, startPosition, endPosition, generateChildren, heuristic):

    initialNode = Node(None, startPosition)
    initialNode.h = initialNode.g =  initialNode.f = 0

    endNode = Node(None, endPosition)
    endNode.h = endNode.g = endNode.f = 0

    openList = [initialNode]
    closedList = []

    while openList:
        currentNode = openList[0]
        currentIndex = 0
        # Calculo el nodo de menor f. (f = g + h)
        for (i, node) in enumerate(openList):
            if node.f < currentNode.f:
                currentNode = node
                currentIndex = i

        openList.pop(currentIndex)
        closedList.append(currentNode)

        if currentNode == endNode:
            path = [currentNode.position]
            while currentNode != initialNode:
                currentNode = currentNode.parent
                path.append(currentNode.position)
            return path[::-1]  # Doy vuelta asi arranca por el nodo inicial.

        # Generar los nodos hijos y agregar
        children = generateChildren(currentNode, maze)

        for child in children:

            isClosed = False
            for closedChild in closedList:
                if closedChild == child:
                    isClosed = True

            if isClosed:
                continue

            if child not in closedList:
                child.g = currentNode.g + 1  # distancia hasta aca + distancia de ir de current a child (entiendo que es 1 porque es 1 movimiento...)
                child.h = heuristic(child.position, endPosition)
                child.f = child.g + child.h

            isOpen = False
            for openNode in openList:
                if child == openNode and child.g > openNode.g:
                    isOpen = True

            if isOpen:
                continue
            openList.append(child)


def heuristic(position, endPosition):
    return ((position[0] - endPosition[0]) ** 2) + ((position[1] - endPosition[1]) ** 2)

def manhattan_distance(pos1, pos2):
  return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def generateChildren(currentNode, maze):
    children = []
    for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:  # Adjacent squares

        # Get node position
        node_position = (currentNode.position[0] + new_position[0], currentNode.position[1] + new_position[1])

        # Make sure within range
        if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (
                len(maze[len(maze) - 1]) - 1) or node_position[1] < 0:
            continue

        # Make sure walkable terrain
        if maze[node_position[0]][node_position[1]] != 0:
            continue

        # Create new node
        new_node = Node(currentNode, node_position)

        # Append
        children.append(new_node)

    return children


def main():

    maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    start = (0, 0)
    end = (7, 6)

    path = astar(maze, start, end, generateChildren, manhattan_distance)
    print(path)

# [(0, 0), (1, 1), (2, 2), (3, 3), (4, 3), (5, 3), (6, 4), (7, 5), (7, 6)]
# [(0, 0), (1, 1), (2, 2), (3, 3), (4, 3), (5, 3), (6, 4), (7, 5), (7, 6)]
if __name__ == '__main__':
    main()