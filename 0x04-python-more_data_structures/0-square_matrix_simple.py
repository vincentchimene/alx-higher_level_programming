#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sq_matrx = ([[a**2 for a in row] for row in matrix])
    return(sq_matrx)
