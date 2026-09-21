import numpy as np
a = np.array([10, 20, 30])
b = np.array([20, 30, 40])

res = np.array(list(set(np.concatenate((a,b)))))
res.sort()
print(res)

import numpy as np
a = np.array([[1, 2], [3, 4], [1, 2], [5, 6]])
res = np.unique(a, axis=0)
print(res)

import numpy as np
a = np.array([1, 2, 2, 3, 3, 3])

res, counts = np.unique(a, return_counts=True)
print("Unique:", res)
print("Counts:", counts)

import numpy as np
a = np.array([3, 1, 2, 1])

unique, inverse = np.unique(a, return_inverse=True)
print("Unique:", unique)
print("Inverse:", inverse)

import numpy as np
a = np.array([4, 3, 3, 2, 1, 2])

unique, indices = np.unique(a, return_index=True)
print("Unique:", unique)
print("Indices:", indices)