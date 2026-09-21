import numpy as np

# 2x3 array filled with ones
arr_one = np.ones((2, 3))
print(arr_one)

import numpy as np

 # 2x3 array of random floats
arr_rand = np.random.rand(2, 3)
print(arr_rand)

import numpy as np

 # 3x3 array of random integers from 1 to 9
arr_int = np.random.randint(1, 10, size=(3, 3))
print(arr_int)

import numpy as np

# Array from 0 to 10 with step 2
arr_range = np.arange(0, 10, 2)
print(arr_range)

import numpy as np

# 5 values from 0 to 1
arr_linspace = np.linspace(0, 1, 5)
print(arr_linspace)

import numpy as np

# Diagonal matrix with [1, 2, 3] on the diagonal
diag_matrix = np.diag([1, 2, 3])
print(diag_matrix)