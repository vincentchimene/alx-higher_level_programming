#!/usr/bin/python3

# a function that prints a matrix of integers.
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
    else:
        for row in range(len(matrix)):
            for item in range(len(matrix[row])):
                if item != len(matrix[row]) - 1:
                    endspace = ' '
                else:
                    endspace = ''
                print("{:d}".format(matrix[row][item]), end=endspace)
            print()
