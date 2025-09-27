import numpy as np

arr_1 = np.array([1,2,3,4,5,6])
print(arr_1)

print("shape: ", arr_1.shape)

print("dimension: ", arr_1.ndim)
print("data type: ", arr_1.dtype)



arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:\n", arr2)
print("Shape:", arr2.shape)




arr3 = np.array([[[1, 2], [3, 4]], 
                [[5, 6], [7, 8]]])
print("3D Array:\n", arr3)
print("Shape:", arr3.shape)




py_list = [2,4,6,8,10]


np_array = np.array([2,4,6,8,10])

py_list_result = [x*2 for x in py_list]

np_array_result = np_array * 2

print(py_list_result)
print(np_array_result)