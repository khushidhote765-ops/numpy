


import numpy as np

arr1 = np.array([[0, 4, 2]])
arr2 = np.array([0.2, 0.4, 2.4])

print("Data type of array 1:", arr1.dtype)
print("Data type of array 2:", arr2.dtype)

import numpy as np
arr = np.array([3, 4, 5, 5])
print(arr)


import numpy as np
text = "Geeksforgeeks"
arr = np.fromiter(text, dtype="U2")
print(arr)

import numpy as np
arr = np.arange(1, 20, 2, dtype=np.float32)
print(arr)

import numpy as np
arr = np.empty((4, 3), dtype=np.int32)
print(arr)


import numpy as np
arr = np.ones((4, 3), dtype=np.int32)
print(arr)