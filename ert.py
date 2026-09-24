import numpy as np

arr = np.array([1, 2, 3])
print(arr)

arr = np.array([[1, 2, 3], [7, 5, 6]])
print(arr)

arr = np.array((1, 3, 2))
print(arr)

import numpy as np
a = np.array([0, 1, 2, 6, 0])
res = np.trim_zeros(a, trim='b')
print(res)

import numpy as np

a = np.array([[1, 2],
              [3, 4]])

b = np.array([[4, 3],
              [2, 1]])

print("Adding 1 to every element:\n", a + 2)
print("Subtracting 2 from each element:\n", b - 5)
print("Sum of all array elements:", a.sum())
print("Array sum:\n", a + b)

import numpy as np

x = np.array([1, 2])
print(x.dtype)

x = np.array([8.0, 7.0])
print(x.dtype)

x = np.array([1, 2], dtype=np.int64)
print(x.dtype)