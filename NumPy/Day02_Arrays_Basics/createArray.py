import numpy as np

# list array
# my_list = [10,20,30,40,50,60,70]
# arr_1 = np.array(my_list)
# print(arr_1)

# # tuple

# tup = (10,20,30,40,50)
# arr_1 = np.array(tup)
# print(arr_1)


# arr_2 = np.array([[[10,20,30,40,50],[60,70,80,90,100]]])
# print(arr_2)


arr_1 = np.array([10,20,30,40,50,60,70])
print(arr_1)
print(arr_1.ndim)


arr_2 = np.array([[10,20,30],[40,50,60]])
print(arr_2.ndim)


arr_= np.arange(0,12,1)
print(arr_)

arr_linspace= np.linspace(0, 1, 10)
print(arr_linspace)



arr_3 =np.array([[[1,2,],[3,4],[5,6]]])
print(arr_3.ndim)
print(arr_3)










# Creating a 1D array
x = np.array([1, 2, 3])

# Creating a 2D array
y = np.array([[1, 2], [3, 4]])

# Creating a 3D array
z = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

print(x)
print(x.shape)
print(x.ndim)
print(x.size)