import numpy as np
arr = np.array([3, 4, 6, 8, 10])
v = arr.view()

print("Original ID:", id(arr))
print("View ID:    ", id(v))

arr[0] = 12

print("Original array:", arr)
print("View array:    ", v)

import numpy as np
arr = np.array([2, 4, 6, 8, 10])
c = arr.copy()

print("Original ID:", id(arr))
print("Copy ID:    ", id(c))

arr[0] = 12
print("Original array:", arr)
print("Copy array:    ", c)

import numpy as np
arr = np.array([2, 4, 6, 8, 10])

c = arr.copy()
v = arr.view()

print(c.base)
print(v.base)