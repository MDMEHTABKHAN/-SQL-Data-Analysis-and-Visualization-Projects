import numpy as np


tensor = np.array([[[1, 2], [3, 4]],
                    [[5, 6], [7, 8]],
                    [[9,10], [11,12]]])
print("Tensor:\n", tensor)
print("Shape:", tensor.shape)

print(tensor[0][0][0])


print(tensor[0][1][0])



print(tensor[1][1][1])

