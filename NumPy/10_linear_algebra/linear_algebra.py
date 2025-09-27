import numpy as np



A = np.array([10,20,30,40])
B = np.array([50,60,70,80])

# C = A + B
# print("\n Addition: ")
# print("addition of tho number A and B: ", C)

# D = B - A
# print("\n Subtraction: ")
# print("Subtraction of tho number B and A: ", D)

# E = A * B
# print("\n Multiplication: ")
# print("Multiplication of tho number A and B: ", E)

# F = B / A 
# print("\n Divide: ")
# print("Divide by of tho number B and A: ", F)

# F = B // A 
# print("\n divided without fraction: ")
# print("Divide by of tho number B and A: ", F)

# elem_multi = A * B
# print("\n Element multiplication: ")
# print(elem_multi)


# dot_mult = np.dot(A,B)
# print("\n dot multiplication: ")
# print(dot_mult)

# dot_mult_2 = A @ B
# print(dot_mult_2)




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