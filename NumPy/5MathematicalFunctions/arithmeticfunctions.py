import numpy as np


arr = np.array([10,20,40,50,60,70,80,90,100])

arr_1 = np.array([5,10,15,20,25,30,35,40,45,50])


print(np.add(arr,arr_1))
print(np.subtract(arr,arr_1))
print(np.multiply(arr,arr_1))
print(np.divide(arr, arr_1))





A = np.array([10,20,30,40])
B = np.array([50,60,70,80])




# AGGREGATION FUNCTION

print("sum of total number from A:", np.sum(A))
print("max number of B:", np.max(B))
print(np.min(A))
print(np.mean(A))
print(np.median(B))
print(np.sqrt(A))
print(np.std(B))





# Arithmetic operation

print("addition: ",np.add(A, B))
print("Subtraction: ",np.subtract(B,A))

print("Multiplication: ", np.multiply(A,B))
print("Divide: ", np.divide(B,A))
print("Power:", np.power(A, B))