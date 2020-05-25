#!/usr/bin/python3
'''Multiplies two matrices'''


def matrix_mul(m_a, m_b):
    '''Usage: matrix_mul(m_a, m_b)'''
    if not isinstance(m_a, list):
        raise TypeError('m_a must be a list')
    elif not isinstance(m_b, list):
        raise TypeError('m_b must be a list')
    elif (len([i for i in range(len(m_a)) if isinstance(m_a[i], list)]) !=
          len(m_a)):
        raise TypeError('m_a must be a list of lists')
    elif (len([i for i in range(len(m_b)) if isinstance(m_b[i], list)]) !=
          len(m_b)):
        raise TypeError('m_b must be a list of lists')
    elif (len([i for i in range(len(m_a)) if m_a[i]]) != len(m_a)):
        raise ValueError('m_a can\'t be empty')
    elif (len([i for i in range(len(m_b)) if m_b[i]]) != len(m_b)):
        raise ValueError('m_b can\'t be empty')
    elif (len([i for i in range(len(m_a)) if all(isinstance(j, (int, float))
                                                 for j in m_a[i])]
              ) != len(m_a)):
        raise TypeError('m_a should contain only integers or floats')
    elif (len([i for i in range(len(m_b)) if all(isinstance(j, (int, float))
                                                 for j in m_b[i])]
              ) != len(m_b)):
        raise TypeError('m_b should contain only integers or floats')
    elif (len([i for i in range(len(m_a)) if len(m_a[i]) == len(m_a[0])])
          != len(m_a)):
        raise TypeError('each row of m_a must be of the same size')
    elif (len([i for i in range(len(m_b)) if len(m_b[i]) == len(m_b[0])])
          != len(m_b)):
        raise TypeError('each row of m_b must be of the same size')
    elif (len(m_a[0]) != len(m_b)):
        raise ValueError('m_a and m_b can\'t be multiplied')
    else:
        return (matrix_multiplier(m_a, m_b))

def matrix_multiplier(m_a, m_b):
    '''Driver function for matrix_mul'''
    res = [ [0 for i in range(len(m_a))] for j in range(len(m_a)) ]
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                res[i][j] += m_a[i][k] * m_b[k][j]
    return (res)
