import numpy as np
a = np.array([10, 20, 30])
b = np.array([60, 70, 40])

res = np.array(list(set(np.concatenate((a,b)))))
res.sort()
print(res)

import numpy as np
from functools import reduce

a = [
    np.array([1, 2, 3]),
    np.array([3, 4, 5]),
    np.array([5, 6, 7]),
    np.array([8, 9, 10])
]

res = reduce(np.union1d, a)
print(res)

import numpy as np
a = np.array([[1, 2, 3], [4, 5, 6], [1, 2, 3], [7, 8, 9]])
b = np.ascontiguousarray(a).view(np.dtype((np.void, a.dtype.itemsize * a.shape[1])))

_, idx = np.unique(b, return_index=True)
res = a[np.sort(idx)]
print(res)

import numpy as np
a = np.array([1, 2, 2, 3, 3, 3])

res, counts = np.unique(a, return_counts=True)
print("Unique:", res)
print("Counts:", counts)

import numpy as np

a = np.array([0, 0, 4, 6, 0, 5, 0, 0])
res = np.trim_zeros(a)
print(res)

import numpy as np
a = np.array([0, 1, 7, 0, 0])
res = np.trim_zeros(a, trim='b')
print(res)