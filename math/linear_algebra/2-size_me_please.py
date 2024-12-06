#!/usr/bin/env python3

def matrix_shape(matrix):
    """ find the shape of Matrix """
    return [len(matrix)] + matrix_shape(matrix[0]) if isinstance(matrix, list) and matrix else []
