from det_matrix import determinant

def solve_Kramer(matrix, b):
    n = len(matrix)
    det = determinant(matrix)
    if det == 0:
        raise ValueError("Система не имеет решений")
    x = [0]*n
    dets = []
    for i in range(n): # перебор по столбцам
        tmp = [[matrix[k][j] if j != i else b[k] for j in range(n)] for k in range(n)]
        det_tmp = determinant(tmp)
        dets.append(det_tmp)
        x[i] = det_tmp/det
    return dets, x
