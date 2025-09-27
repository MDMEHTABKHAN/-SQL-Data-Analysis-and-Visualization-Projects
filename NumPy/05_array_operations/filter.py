import numpy as np



num_arr = np.array([5,3,6,7,8,10,30,40,60,70,90,10])
even_number = num_arr[num_arr % 2 == 0]
print(even_number)


greater_than_five = even_number[even_number > 5]
print(greater_than_five)



mask = num_arr[num_arr > 5]
# mask = num_arr > 5
print(mask)

