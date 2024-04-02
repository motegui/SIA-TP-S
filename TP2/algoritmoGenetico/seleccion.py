def elite(poblacion, size):
    poblacion_len = len(poblacion)
    nueva_poblacion = []
    sorted_poblacion = sorted(poblacion, key=lambda x: x.desempeno(), reverse=True)
    iter = 0

    while iter != size:
        nueva_poblacion.append(sorted_poblacion[iter % poblacion_len])
        iter += 1
    return nueva_poblacion
