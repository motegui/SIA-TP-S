def iterate_within_radius(matrix, center, radius):
    result = []
    rows, cols = len(matrix), len(matrix[0])
    center_row, center_col = center
    print(radius)
    for i in range(center_row - radius, center_row + radius + 1):
        for j in range(center_col - radius, center_col + radius + 1):
            if 0 <= i < rows and 0 <= j < cols and ((i - center_row) ** 2 + (j - center_col) ** 2) <= radius ** 2:
                result.append(matrix[i][j])

    return result
