import numpy as np

vector = np.arange(2, 6)
print("Vector using np.arange():", vector)

import numpy as np

vector = np.linspace(0, 11, 5)

print("Vector using np.linspace():", vector)

import numpy as np

vector_zeros = np.zeros(4)
print("Vector using np.zeros():", vector_zeros)

vector_ones = np.ones(4)
print("Vector using np.ones():", vector_ones)

import numpy as np

list1 = [6, 7, 9]
list2 = [1, 4, 5]

vector1 = np.array(list1)

print("First Vector          : " + str(vector1))

vector2 = np.array(list2)

print("Second Vector         : " + str(vector2))

addition = vector1 + vector2
print("Vector Addition       : " + str(addition))

subtraction = vector1 - vector2
print("Vector Subtraction   : " + str(subtraction))

multiplication = vector1 * vector2
print("Vector Multiplication : " + str(multiplication))

division = vector1 / vector2
print("Vector Division       : " + str(division))