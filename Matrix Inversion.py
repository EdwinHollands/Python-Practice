import numpy as np

def determinant(matrix):
    # Check if the matrix is square
    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError("Determinant is only defined for square matrices.")
    
    if matrix.shape == (1, 1):
        return matrix[0, 0]
    if matrix.shape == (2, 2):
        return matrix[0, 0] * matrix[1, 1] - matrix[0, 1] * matrix[1, 0]
    det = 0
    for i in range(matrix.shape[1]):
        submatrix = np.delete(np.delete(matrix, 0, axis=0), i, axis=1)
        det += matrix[0, i] * ((-1) ** i) * determinant(submatrix)
    return det

def inverse(matrix):
    det = determinant(matrix)
    if det == 0:
        raise ValueError("Matrix is singular and cannot be inverted.") 
    adjugate = np.zeros_like(matrix)
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            submatrix = np.delete(np.delete(matrix, i, axis=0), j, axis=1)
            adjugate[j, i] = ((-1) ** (i + j)) * determinant(submatrix)
    return adjugate / det
M = np.array([[1, 2], [3, 4]])
print(inverse(M))
I = M @ inverse(M)
print(I)
print('test')