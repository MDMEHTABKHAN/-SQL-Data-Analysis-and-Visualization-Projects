import numpy as np


arr = np.array([1, 2, 3, 4])
view = arr[1:3]   # view of arr
print(view)
view[0] = 99
print(arr)   # [ 1 99  3  4]  (original changed!)





arr = np.array([1, 2, 3, 4])
copy = arr[1:3].copy()
copy[0] = 99
print(arr)   # [1 2 3 4]   (original not changed)
