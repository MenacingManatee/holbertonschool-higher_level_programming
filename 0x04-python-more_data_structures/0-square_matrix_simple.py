#!/usr/bin/python3
def square(n):
    return (n * n)


def square_matrix_simple(matrix=[]):
    res = []
    for li in range(0, len(matrix)):
        res.append(list(map(square, matrix[li])))
    return (res)
