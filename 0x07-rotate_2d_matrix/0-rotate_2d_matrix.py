#!/usr/bin/python3
"""Module Rotate 2D Matrix"""


def rotate_2d_matrix(matrix):
    """Rotate a 2D matrix"""
    n = len(matrix)
    for i in range(n // 2):
        last = n - 1 - i
        for j in range(i, last):
            offset = j - i
            tmp = matrix[i][j]
            matrix[i][j] = matrix[last - offset][i]  # bottom to top
            matrix[last - offset][i] = matrix[last][last - offset]
            # right to bottom
            matrix[last][last - offset] = matrix[j][last]  # top to right
            matrix[j][last] = tmp  # left to top
