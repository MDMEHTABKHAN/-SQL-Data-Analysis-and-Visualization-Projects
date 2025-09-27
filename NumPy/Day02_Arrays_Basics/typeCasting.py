import numpy as np



# type casting

arr_1 = np.array([1.1,2.3,4.5])

print(type(arr_1))

arr_int = arr_1.astype(int)
print(arr_int)

arr_str = arr_int.astype(str)
print(arr_str)


arr_str_1 = arr_1.astype(str)
print(arr_str_1)

