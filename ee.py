import numpy as np

# Create a 1D array of zeros with 5 elements
arr = np.zeros(6)
print(arr)

import numpy as np
arr = np.zeros((2, 3))
print(arr)

import numpy as np
arr = np.zeros((3, 4), dtype=int)
print(arr)

import numpy as np
arr = np.zeros((1, 2), order='F')
print(arr)

import numpy as np

list1 = [1, 2, 3]
list2 = [[40],
        [50],
        [60]]
vector1 = np.array(list1)
vector2 = np.array(list2)

print("Horizontal Vector")
print(vector1)

print("----------------")

print("Vertical Vector")
print(vector2)