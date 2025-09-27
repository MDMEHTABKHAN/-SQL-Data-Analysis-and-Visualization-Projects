import numpy as np
matrix = np.array([[1, 2, 3],
                [4, 5, 6]])
print("Matrix:\n", matrix)
print("Shape:", matrix.shape)



arr2 = np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])

print(arr2)
print(arr2, arr2.ndim)
print(arr2.shape)
print(arr2.size)
print(arr2.itemsize)

print(np.sum(arr2, axis=0))

print(np.sum(arr2, axis=1))
print(np.sum(arr2))



array = np.array('A')
print(array.ndim)

