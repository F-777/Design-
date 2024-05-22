import numpy as np

# Create a 2x2 complex matrix with zeros as elements
complex_matrix = np.zeros((2, 2), dtype=complex)

# Assign complex values to the matrix
complex_matrix[0, 0] = 1 + 2j
complex_matrix[0, 1] = 3 - 4j
complex_matrix[1, 0] = -2 + 1j
complex_matrix[1, 1] = 0.5 + 0.5j

# Print the complex matrix
print("Complex Matrix:")
print(complex_matrix)

# Access individual elements
print("Element at (0, 1):", complex_matrix[0, 1])

# Compute the conjugate of the matrix
conjugate_matrix = np.conjugate(complex_matrix)
print("Conjugate Matrix:")
print(conjugate_matrix)

# Multiply matrices (dot product)
identity_matrix = np.eye(2, dtype=complex)
result_matrix = np.dot(complex_matrix, identity_matrix)
print("Result of matrix multiplication:")
print(result_matrix)
