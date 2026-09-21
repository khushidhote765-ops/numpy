import numpy as np
a = np.linspace(1, 3, num=10)
print(a)

import numpy as np
b = np.linspace(0,  3, num=10, endpoint=False)
print(b)

import numpy as np
array, c = np.linspace(0, 11, num=5, retstep=True)
print("Step Size:", c)

import numpy as np
d = np.linspace(0, 2, num=16).reshape(4, 4)
print(d)

import numpy as np

# Creating a 3x3 identity matrix
identity_matrix = np.eye(5)
print(identity_matrix)

import numpy as np

# Creating a 3x5 rectangular matrix
rectangular_matrix = np.eye(2, 5)
print(rectangular_matrix)