#!/usr/bin/env python3
matrix = [[1, 3, 9, 4, 5, 8], [2, 4, 7, 3, 4, 0], [0, 3, 4, 6, 1, 5]]

the_middle = [[row[len(row) // 2 - 1], row[len(row) // 2]] if len(row) %
              2 == 0 else [row[len(row) // 2]] for row in matrix]
print("The middle columns of the matrix are: {}".format(the_middle))