import numpy as np

list1 = [4, 5, 9]
list2 = [6, 7, 3]

vector1 = np.array(list1)
print("First Vector  : " + str(vector1))

vector2 = np.array(list2)
print("Second Vector : " + str(vector2))

dot_product = vector1.dot(vector2)
print("Dot Product   : " + str(dot_product))

import numpy as np

list1 = [6, 5, 4]

vector = np.array(list1)
print("Vector  : " + str(vector))

scalar = 2
print("Scalar  : " + str(scalar))

scalar_mul = vector * scalar
print("Scalar Multiplication : " + str(scalar_mul))