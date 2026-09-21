import numpy as np

a = [1, 2, 3, 4]
arr = np.array(a)

print("List: ", a)
print("Numpy Array:", arr)
print(type(a))
print(type(arr))


import numpy as np

l1 = [1, 2, 3, 4]
l2 = [5, 6, 7, 8]
l3 = [9, 10, 11, 12]
arr = np.array([l1, l2, l3])
print(arr)


import numpy as np
arr = np.array([ [0, 4, 2],
                 [3, 4, 5],
                 [23, 4, 5],
                 [2, 34, 5],
                 [5, 6, 7] ])
print(arr.shape)