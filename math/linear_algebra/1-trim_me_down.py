#!/usr/bin/env python3
matrix = [[1, 3, 9, 4, 5, 8], [2, 4, 7, 3, 4, 0], [0, 3, 4, 6, 1, 5]]
the_middle = [None] * len(matrix)

for i in range(len(matrix)):
    row = matrix[i]

    if len(row) % 2 == 0:

        middle = [row[len(row) // 2 - 1], row[len(row) // 2]]

    else:
        middle = row[len(row) // 2]

    the_middle[i] = middle
print("The middle columns of the matrix are: {}".format(the_middle))
