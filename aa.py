import numpy as np

arr = np.arange(5*5).reshape(5, 5)
print(arr.shape)

# promoting 2D array to a 5D array
# arr[None, ..., None, None]
arr_5D = arr[np.newaxis, ..., np.newaxis, np.newaxis]

print(arr_5D.shape)

import numpy as np

x = np.zeros((3, 5))
y = np.expand_dims(x, axis=1).shape
print(y)

import numpy as np

arr = np.arange(5*5).reshape(5,5)
print(arr.shape)

newaxes = (0, 3, -1)
arr_5D = np.expand_dims(arr, axis=newaxes)
print(arr_5D.shape)

import numpy as np
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

res = np.hstack((a, b))
print(res)

import numpy as np
a = np.array([-1, -2, -3])
b = np.array([4, 5, 7])

res = np.hstack((a, b))
print(res)