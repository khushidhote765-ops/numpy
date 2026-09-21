import numpy as np

dt = np.dtype([ ('name', np.str_, 16), ('scores', np.float64, (2,)) ])
data = np.array([ ('Emma', (8.5, 7.0)), ('Lucas', (6.0, 7.5)) ], dtype=dt)

print(data[1])
print("Scores:", data[1]['scores'])
print("Names:", data['name'])


import numpy as np

a = np.array([1])
print("type:", type(a))
print("dtype:", a.dtype)

import numpy as np

# One-dimensional array
arr1 = np.array([1, 2, 3, 4, 5])
print(arr1)

# Two-dimensional array
arr2 = np.array([[1, 2], [3, 4]])
print(arr2)

import numpy as np

# 3x4 array filled with zeros
arr_zero = np.zeros((3, 4))
print(arr_zero)