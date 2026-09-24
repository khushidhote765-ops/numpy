import numpy as np
a = np.arange(12).reshape(4, 3)
print("Original array:\n", a)

res = a.copy()
res[:, [0, 2]] = res[:, [2, 0]]
print("After swapping:\n", res)

import numpy as np
arr = np.arange(6)
arr_reshape = arr.reshape((2, 3))

import numpy as geek

a = geek.array([[ 1, 2, 3], [ -4, -5, -3]] )
print ("1st Input array : \n", a)

b = geek.array([[ 4, 5, 6], [ -4, -8, -7]] )
print ("2nd Input array : \n", b)

res = geek.vstack((a, b))
print ("Output stacked array :\n ", res)

import numpy as np
a = np.array([1, 5])
b = np.array([3, 6])

res = np.concatenate((a, b))
print(res)