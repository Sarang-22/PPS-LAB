import numpy as np

# Read dimension
n = int(input("dimension: "))

# Read first matrix
print("first matrix:")
A = np.array([list(map(int, input().split())) for _ in range(n)])

# Read second matrix
print("second matrix:")
B = np.array([list(map(int, input().split())) for _ in range(n)])

# Multiply matrices
C = np.dot(A, B)

# Print result
print("Resultant Matrix:")
for row in C:
	print(*row)
