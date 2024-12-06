#!/usr/bin/env python3
""" returns the transpose of a 2D matrix """


def matrix_transpose(matrix):
    """ function that returns the transpose of a 2D matrix """
    a = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
    return matrix
