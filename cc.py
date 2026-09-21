import numpy as geek

a = geek.array([[ 1, 2, 3], [ -1, -2, -3]] )
print ("1st Input array : \n", a)

b = geek.array([[ 4, 5, 6], [ -4, -5, -6]] )
print ("2nd Input array : \n", b)

res = geek.vstack((a, b))
print ("Output stacked array :\n ", res)

import numpy as np
a = np.array([1, 2])
b = np.array([3, 4])

res = np.concatenate((a, b))
print(res)

import numpy as np
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

res_h = np.hstack((a, b))
print("np.hstack: ", res_h)

res_v = np.vstack((a, b))
print("np.vstack: ", res_v)

res_d = np.dstack((a,b))
print("np.dstack: ", res_d)

import numpy as np
b1 = np.array([[1, 1], [1, 1]])
b2 = np.array([[2, 2, 2], [2, 2, 2]])
b3 = np.array([[3, 3], [3, 3], [3, 3]])
b4 = np.array([[4, 4, 4], [4, 4, 4], [4, 4, 4]])

res = np.block([
    [b1, b2],
    [b3, b4]
])

print(res)