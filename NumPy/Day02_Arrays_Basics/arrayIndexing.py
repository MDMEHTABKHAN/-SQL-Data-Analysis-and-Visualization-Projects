import numpy as np


arr_1 = np.array([10,20,30,40,50,60,70])


print(arr_1[0])

print(arr_1[3])



arr_2 = np.array([[10,20,30],[40,50,60]])

print(arr_2[0,1])
print(arr_2[0,0])


print(arr_2[1,0])
print(arr_2[1,2])



arr_3 = np.array([[[10,20,30],[40,50,60],[70,80,90]]])

print(arr_3[0,0,0])
print(arr_3[0,0,1])
print(arr_3[0,0,2])



print(arr_3[0,1,0])
print(arr_3[0,1,1])
print(arr_3[0,1,2])

print(arr_3[0,2,0])
print(arr_3[0,2,1])
print(arr_3[0,2,2])


