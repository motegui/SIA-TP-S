def read_file(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
    return [line.removesuffix('\n') for line in lines]


def process_map(map):
    matrix_1 = []
    matrix_2 = []
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
            elif map[i][j] == '.':
                row_1.append(ord(' '))
                row_2.append(ord('$'))
            elif map[i][j] == '*':
                row_1.append(ord('$'))
                row_2.append(ord('$'))
            else:
                row_1.append(ord(map[i][j]))
                row_2.append(ord(map[i][j]))

        matrix_1.append(row_1)
        matrix_2.append(row_2)

    return matrix_1, matrix_2, start_position


# def imprimir_mapa():
#     # Nombre del archivo de texto
#     nombre_archivo = "mapa.txt"
#
#     # Leer el archivo
#     mapa = leer_archivo(nombre_archivo)
#
#     # Procesar el mapa
#     matriz_1, matriz_2, posicion_arroba = procesar_mapa(mapa)
#     print("Matriz 1:")
#     for fila in matriz_1:
#         fila_caracteres = [chr(numero) for numero in fila]
#         print(' '.join(fila_caracteres))
#
#     print("Matriz 2:")
#     for fila in matriz_2:
#         fila_caracteres = [chr(numero) for numero in fila]
#         print(' '.join(fila_caracteres))
#
#     print(posicion_arroba)
#
#
# if __name__ == '__main__':
#     imprimir_mapa()
