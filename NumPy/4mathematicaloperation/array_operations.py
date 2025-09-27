import numpy as np


a = np.array([2, 4, 6, 8])
b = np.array([1, 3, 5, 7])


print("addition:",  a + b)
print("subtraction: ", a -b)
print("multiplication: ", a * b)
print("Division: ", a / b)


arr = np.array([10, 20, 30, 40])

print("multiply by 2: ", arr*2)
print("subtract by 5: ", arr-5 )


arr2d = np.array([[1, 2, 3],
                [4, 5, 6]])
col_vec = np.array([[10],
                    [20]])

print(arr2d + col_vec)




scores = np.array([[50, 60, 70],
                [80, 90, 100],
                [65, 75, 85]])

# Find max of each column
max_scores = scores.max(axis=0)

# Normalize
normalized = scores / max_scores

print("\nOriginal Scores:\n", scores)
print("Max scores per column:", max_scores)
print("Normalized Scores:\n", normalized)
