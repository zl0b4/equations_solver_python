def det2(matrix):
    """ Возвращает определитель второго порядка """

    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def minor(matrix, i, j):
    """ Возвращает дополнительный минор к элементу i, j """

    tmp = [row for k, row in enumerate(matrix) if k != i]
    # print(tmp)
    # print(list(zip(*tmp)))
    tmp = [col for k, col in enumerate(zip(*tmp)) if k != j]
    # print(tmp)
    return tmp
    # return list(zip(*tmp))


def determinant(matrix):
    """ Возвращает определитель квадратной матрицы n-го порядка"""

    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    elif n == 2:
        return det2(matrix)

    return sum((-1) ** j * matrix[0][j] * determinant(minor(matrix, 0, j))
               for j in range(n))


def det3(matrix):
    """ Возвращает определитель квадратной матрицы 3-го порядка"""

    return sum((-1) ** j * matrix[0][j] * det2(minor(matrix, 0, j))
               for j in range(3))


def det4(matrix):
    """ Возвращает определитель квадратной матрицы 4-го порядка"""

    return sum((-1) ** j * matrix[0][j] * det3(minor(matrix, 0, j))
               for j in range(4))

