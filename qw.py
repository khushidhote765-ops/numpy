import numpy as np
arr = np.array([3, 4, 7, 8, 10])

c = arr.copy()
v = arr.view()

print(c.base)
print(v.base)

# importing Numpy package
import numpy as np

# Creating a numpy array using np.array()
org_array = np.array([2.54, 3.99, 4.42, 5.87, 6.94,
                      9.21, 7.65, 10.50, 77.5])

print("Original array: ")

# printing the Numpy array
print(org_array)

# Now copying the org_array to copy_array
# using np.copy() function
copy_array = np.copy(org_array)

print("\nCopied array: ")

# printing the copied Numpy array
print(copy_array)

# importing the module
import numpy as np

arr1 = np.array([[4, 2], [5, 4]])
arr2 = np.array([[8, 6]])

combined = np.concatenate((arr1, arr2), axis=0)
print(combined)