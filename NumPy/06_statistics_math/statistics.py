import numpy as np


import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])


# column wise axis = 0

print("COLUMN WISE OPERATION \n")
print(np.sum(arr, axis = 0)) #[12,15,18]
print(np.mean(arr, axis = 0))
print(np.max(arr, axis = 0))
print(np.min(arr, axis = 0))



# row wise axis = 1

print("ROW WISE OPERATION \n")
print(np.sum(arr, axis = 1)) #[6,15,24]
print(np.mean(arr, axis = 1))
print(np.min(arr, axis= 1))
print(np.max(arr, axis = 1))


#  no axis

print(np.sum(arr))   # 45
print(np.mean(arr))  # 5.0
print(np.min(arr))   # 1
print(np.max(arr))   # 9




arr = np.array([1, 2, 3, 4, 5])

print("Mean:", np.mean(arr))        # sum of total number/ number element = 15/5 = 3.0
print("Variance:", np.var(arr))     # 2.0
print("Standard Deviation:", np.std(arr))  # 1.4142







