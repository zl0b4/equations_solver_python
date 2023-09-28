from det_matrix import determinant, minor


def inverse_matrix(matrix):
    n = len(matrix)
    if n != len(matrix[0]):
        raise ValueError("Матрица должна быть квадратной")

    inv = [[0] * n for _ in range(n)]

    det = determinant(matrix)
    print(f"det={det}")

    if det:
        for i in range(n):
            for j in range(n):
                m = minor(matrix, i, j)

                # автоматическое транспонирование, так как присваиваем минор для i,j элемента в j,i
                inv[j][i] = round((-1) ** (i + j) * determinant(m), 2)

        return det, inv
    else:
        raise ValueError("Матрица вырожденная")


# n = int(input("Введите порядок матрицы: "))
# matrix = [list(map(int, input().split())) for _ in range(n)]
#
# det, inv = inverse_matrix(matrix)
# print("1/"+str(det), end='*')
# print(*inv, sep='\n\t')
