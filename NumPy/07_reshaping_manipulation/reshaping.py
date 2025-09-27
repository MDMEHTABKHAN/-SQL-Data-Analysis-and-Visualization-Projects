import numpy as np



array = np.arange(1,13)
reshaprd_arr =array.reshape(3,4)
print(reshaprd_arr)

reshaprd_arr3d = array.reshape(2,2,3)
print("reshaped_3d array: ",reshaprd_arr3d)


print(array)
print(np.sqrt(array))
print(np.sum(array))

print(np.min(array))
print(np.max(array))
print(array.shape)
print(array.itemsize)
print(array.ndim)
print(array.size)

