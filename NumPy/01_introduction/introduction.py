import numpy as np

print(np.__version__)
# create simple array
array = np.array([1,2,3,4,5])
print(array)



arr = np.array([10,20,30,40,50,60,3,4,5,7])



print("sum: ", arr.sum())

# Mean, Sum, Standard Deviation
print("Mean:", np.mean(arr))
print("Sum:", np.sum(arr))
print("Standard Deviation:", np.std(arr))



py_list = [20,3,4]
arr_list = np.array(py_list)
print(arr_list)


tup = (10,20,3,45)

arr_tup = np.array(tup)
print(arr_tup)