from TP1.utils.state import State


def read_file(file_name):
    with open(file_name, "r") as file:
        lines = file.read().split('\n')
    #search for the max length in lines
    length = max(len(line) for line in lines)
    matrix = []
    for line in lines:
        padded_line = line.ljust(length, '#')
        row = list(padded_line)
        matrix.append(row)

    return matrix


def process_map(map):
    matrix_1 = []
    matrix_2 = []
    box_positions = []
    goal_positions = []
    start_position = None

    for i in range(len(map)):
        row_1 = []
        row_2 = []
        for j in range(len(map[i])):
            if map[i][j] == '@':
                start_position = (i, j)
                row_1.append(ord(' '))
                row_2.append(ord(' '))
            elif map[i][j] == '$':
                row_1.append(ord(map[i][j]))
                row_2.append(ord(' '))
                box_positions.append((i, j))
            elif map[i][j] == '.':
                row_1.append(ord(' '))
                row_2.append(ord('$'))
                goal_positions.append((i, j))
            elif map[i][j] == '*':
                row_1.append(ord('$'))
                row_2.append(ord('$'))
            else:
                row_1.append(ord(map[i][j]))
                row_2.append(ord(map[i][j]))

        matrix_1.append(row_1)
        matrix_2.append(row_2)
    state = State(matrix_1, goal_positions, box_positions)
    end_state = State(matrix_2, goal_positions, goal_positions)
    return state, end_state, start_position

