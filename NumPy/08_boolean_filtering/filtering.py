import numpy as np


arr_1d = np.array([10,20,30,40,50,60,70,80])

bool_idx = arr_1d > 45
print(bool_idx)
bool_idx = arr_1d[arr_1d > 23]

print(bool_idx)


less_than_40 = arr_1d[arr_1d < 40]
print(less_than_40)



divided_by_3 = arr_1d[arr_1d % 3 == 0]
print(divided_by_3)

