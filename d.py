import numpy as np
arr = np.arange(13)
res = np.array_split(arr, 4)
print(res)

import numpy as np

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[1, 2], [3, 4]])

dif = arr1 == arr2
b = dif.all()
print(b)

import numpy as np

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[1, 2], [3, 4]])

if np.array_equal(arr1, arr2):
    print("Equal")
else:
    print("Not Equal")

    import numpy as np

    a = np.array([101, 99, 87])
    b = np.array([897, 97, 111])

    print("Array a:", a)
    print("Array b:", b)

    print("a > b:", np.greater(a, b))
    print("a >= b:", np.greater_equal(a, b))
    print("a < b:", np.less(a, b))
    print("a <= b:", np.less_equal(a, b))