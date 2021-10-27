from scipy import linalg
import numpy as np
import sympy as sp


A = np.array([[-1, 5, 4, 5], [5, 5, -2, -3], [1, -2, 5, 2], [12, 24, -12, -8]])
det = sp.Matrix(A).det()
print(det)
rank = np.linalg.matrix_rank(A)
print(rank)
A_rref = sp.Matrix(A).rref()
print(A_rref)
