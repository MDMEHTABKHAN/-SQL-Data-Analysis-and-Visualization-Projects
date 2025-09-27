import numpy as np

arr_1 = np.array([1,2,3,4,5])
print("original data type: ", arr_1)


arr_float = arr_1.astype(float)
print(arr_float)


arr_string = arr_1.astype(str)
print(arr_string)


arr_boolean = arr_1.astype(bool)
print(arr_boolean)

