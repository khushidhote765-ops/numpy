# importing the module
import numpy as np

# creating an array
arr1 = np.array([1, 2, 3])
print('First array is : ', arr1)

# creating another array
arr2 = np.array([7, 8, 6])
print('Second array is : ', arr2)

# appending arr2 to arr1
arr = np.append(arr1, arr2)
print('Array after appending : ', arr)

import numpy as np
a = np.arange(12).reshape(4, 3)
print("Original array:\n", a)

a[:, [0, 2]] = a[:, [2, 0]]
print("After swapping:\n",a)

import numpy as np
a = np.arange(12).reshape(4, 3)
print("Original array:\n", a)

res = a.copy()
res[:, [0, 2]] = res[:, [2, 0]]
print("After swapping:\n", res)