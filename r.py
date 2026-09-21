import numpy as np
a = np.array([0, 0, 1, 2, 3, 0])
res = np.trim_zeros(a, trim='f')
print(res)

import numpy as np
a = np.array([0, 1, 2, 0, 0])
res = np.trim_zeros(a, trim='b')
print(res)

import numpy as np
a = np.array([0, 0, 0, 0])
res = np.trim_zeros(a)
print(res)