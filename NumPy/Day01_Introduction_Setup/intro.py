import numpy as np
# import numpy as pd

arr = np.array([10,20,30,40,50,60,70,80])
arr_1 = np.array([2,4,6,8,10,12,14,16])
# print(arr)

print(arr + arr_1)
print(arr - arr_1)
print(arr * arr_1)
print(arr / arr_1)
print(arr ** arr_1)

arr_2= np.array([[[10,20,30,40,50,60], [1,2,3,4,6,7]]])
print(arr_2)

arr_3 = np.array([[[1,2,3],[4,5,6],[7,8,9]]])
print(arr_3)



sum = arr_3 + 3
print(sum)


mul = arr_3 + 2
print(mul)

sub = arr_2 - 1
print(sub)

divided = arr_3 ** 2
print(divided)

