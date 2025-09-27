import numpy as np


arr = np.arange(1,12,2)
print(arr)

arr_1 = np.arange(1,100,2)
print(arr_1)



arr_2 = np.linspace(1, 3, 5)
print(arr_2)



arr_3 = np.linspace(0,1,10)
print(arr_3)



arr = np.identity(3)
print(arr)



arr = np.eye(3, 4, k=0)   # 3x4 matrix, diagonal at k=0
print(arr)

arr2 = np.eye(3, 4, k=1)  # diagonal shifted right
print(arr2)
