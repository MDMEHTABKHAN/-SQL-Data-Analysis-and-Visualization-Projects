import numpy as np


arr = np.array([10,20,30,40])

arr_1 = np.array([5,8,9,12])


print("Addition: ", arr + arr_1)
print("Subtraction: ", arr - arr_1)
print("Multiplication: ", arr * arr_1)
print("Division: ", arr / arr_1)


print("Modulus: ", arr % arr_1)
print("Exponentiation: ", arr ** 2)
print("Floor Division: ", arr // arr_1)
print("Square Root: ", np.sqrt(arr))




print(arr+10)
print(arr-2)
print(arr*3)


print(arr > 10)

print(arr < 30)
print(arr == 20)

print(arr[arr > 20])
