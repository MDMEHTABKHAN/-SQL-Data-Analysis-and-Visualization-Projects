

import numpy as np

array = np.array([100,1,2,12,645,65,76,12,11,23,22,23])


sorted = np.sort((array))
print(sorted)

greater_than_20 = sorted[sorted > 20]
print(greater_than_20)