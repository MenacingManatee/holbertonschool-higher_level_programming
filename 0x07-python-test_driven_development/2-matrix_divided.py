#!/usr/bin/python3
'''Divides all elements in a matrix by div'''


def matrix_divided(matrix, div):
    '''Usage: matrix_divided(matrix, divisor'''
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError('div must be a number')
    if div is 0:
        raise ZeroDivisionError('division by zero')
    if isinstance(matrix, list):
        l = len(matrix[0])
        for i in matrix:
            if len(i) is not l:
                raise TypeError('Each row of the matrix must have the same \
size')
            if not isinstance(i, list):
                raise TypeError('matrix must be a matrix (list of lists) of \
integers/floats')
            for j in i:
                if not isinstance(j, int) and not isinstance(j, float):
                    raise TypeError('matrix must be a matrix (list of lists) \
of integers/floats')
        return(matrix_div_drive(matrix, div))
    raise TypeError('matrix must be a matrix (list of lists) of \
integers/floats')


def matrix_div_drive(matrix, div):
    '''Driver function for matrix_divided'''
    res = []
    for l in matrix:
        res.append([round(i / div, 2) for i in l])
    return (res)
