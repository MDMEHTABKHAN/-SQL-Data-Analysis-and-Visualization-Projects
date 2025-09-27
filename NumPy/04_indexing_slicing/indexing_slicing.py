import numpy as np

arr_1 = np.array([10,20,30,40,50,60,70,80,90])

# indexing

print(arr_1[1])
print(arr_1[2])
print(arr_1[3])
print(arr_1[4])
print(arr_1[5])
print(arr_1[0])
print(arr_1[-1])
print(arr_1[-2])


# slicing

print(arr_1[1:2])
print(arr_1[1:5])
print(arr_1[2:])
print(arr_1[:5])

print(arr_1[-4:-1])
print(arr_1[-6:])


print(arr_1[::4])




arr_2 = np.array([[1,2,3,4],[5,6,7,8]])



print(arr_2[0,0])
print(arr_2[0,2])


print(arr_2[1,0])
print(arr_2[1,3])


print(arr_2[0:2, 1:3])
