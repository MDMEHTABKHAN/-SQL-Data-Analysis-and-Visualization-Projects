import numpy as np


arr_1 = np.array([10,20,30,40,50,60,70])

print(arr_1.sum())

print(arr_1.min())
print(arr_1.max())

print(arr_1.mean())
print(arr_1.std())



arr_2 = np.array([[1,2,3],[4,5,6],[7,8,9]])

print(arr_2.sum())

print(arr_2.sum(axis=0))
print(arr_2.sum(axis=1))

