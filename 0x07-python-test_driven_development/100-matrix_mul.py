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
    elif (len([i for i in range(len(m_b)) if m_a[i]]) != len(m_b)):
        raise ValueError('m_b can\'t be empty')
    elif (len([i for i in range(len(m_a)) if all(isinstance(j, (int, float))
                                                 for j in m_a[i])]
          ) != len(m_a)):
        raise TypeError('m_a should contain only integers or floats')
