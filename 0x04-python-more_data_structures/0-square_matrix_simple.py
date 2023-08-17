#!/usr/bin/python3

""" Write a function that computes
the square value of all integers of a matrix.
Prototype: def square_matrix_simple(matrix=[]):
"""
def square_matrix_simple(matrix=[]):
    new_matrix = ([[a**2 for a in row] for row in matrix])
    return (new_matrix)
