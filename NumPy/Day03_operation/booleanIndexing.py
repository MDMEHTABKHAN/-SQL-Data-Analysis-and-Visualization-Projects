import numpy as np

arr_2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])



print(arr_2[::-1])


# print(arr_2 > 5)

print(arr_2[arr_2 > 5])


print(arr_2[arr_2 % 2 == 0])