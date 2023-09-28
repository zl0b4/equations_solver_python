from inverse_matrix import inverse_matrix


def solve_matrix_method(matrix, b):
    det, inv = inverse_matrix(matrix)
    n = len(matrix)

    x = [0] * n

    for i in range(n):
        for j in range(n):
            x[i] += inv[i][j] * b[j]
        x[i] /= det
    return x