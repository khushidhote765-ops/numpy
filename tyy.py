import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11,12,]])
res = np.hsplit(arr, 2)
print(res)

import numpy as np

num1 = np.array([1, 2])
num2 = np.array([[10, 20],
                 [40, 50]])

for a, b in np.nditer([num1, num2]):
    print(a, ":", b)

import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

res = np.dstack((a, b))
print(res)

import numpy as np
a = np.array([1, 2, 3])
b = np.array([7, 8, 6])

res = np.hstack((a, b))
print(res)

# importing the module
import numpy as np

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6]])

combined = np.concatenate((arr1, arr2), axis=0)
print(combined)

import numpy as np
arr = np.array([3, 4, 9, 7, 10])

c = arr.copy()
v = arr.view()

print(c.base)
print(v.base)

import numpy as np
a = np.array([0, 0, 1, 5, 3, 0])
res = np.trim_zeros(a, trim='f')
print(res)

import numpy as np

arr1 = np.array([[4, 7], [2, 6]], dtype=np.float64)
arr2 = np.array([[3, 6], [2, 8]], dtype=np.float64)

print(np.add(arr1, arr2))
print(np.sum(arr1))
print(np.sqrt(arr1))
print(arr1.T)