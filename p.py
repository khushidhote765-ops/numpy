import numpy as np

num1 = np.arange(7)
print("1D array:")
print(num1)

num2 = np.arange(21).reshape(3, 7)
print("\n2D array:")
print(num2)

for a, b in np.nditer([num1, num2]):
    print("%d:%d" % (a, b))

    import numpy as np

    a = np.ma.array([[100, 200], [300, 400]], mask=[[0, 1], [0, 0]])
    b = np.ma.array([[500, 600]], mask=[[1, 0]])

    res = np.ma.concatenate([a, b], axis=0)
    print(res)

    import numpy as np

    a = np.array([-1, -2, -3])
    b = np.array([4, 5, 6])

    res = np.dstack((a, b))
    print(res)