# Imports matrix, matmul and diag functions only
from numpy import matrix
from numpy import matmul
from numpy import diag

# Imports svd function from linalg (linear algebra) submodule of scipy
from scipy.linalg import svd

# Define a matrix
A = matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Matrix A:\n", A)

# Singular-value decomposition
# A is decomposed into 3 matrices: U, a diagonal matrix (S), and V
# Here S contains only the diagonal elements of the diagonal matrix
U, S, V = svd(A)

print("\nMatrix U:\n", U)
print("\nSingular values S:\n", S)
print("\nMatrix V:\n", V)

# Create diagonal matrix from diagonal elements
Sigma = diag(S)
print("\nDiagonal matrix Sigma:\n", Sigma)

# Reconstruct the original matrix
B = matmul(U, matmul(Sigma, V))
print("\nReconstructed Matrix B:\n", B)
