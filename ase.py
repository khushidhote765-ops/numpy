import numpy as np

num1 = np.arange(5)
print("1D array:")
print(num1)

num2 = np.arange(10).reshape(2, 5)
print("\n2D array:")
print(num2)

# Combine 1-D and 2-D arrays
for a, b in np.nditer([num1, num2]):
    print("%d:%d" % (a, b))

    import numpy as np

    a = np.ma.array([[100, 300], [400, 600]], mask=[[0, 1], [0, 0]])
    b = np.ma.array([[500, 600]], mask=[[1, 0]])

    res = np.ma.concatenate([a, b], axis=0)
    print(res)

    import numpy as np

    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])

    res = np.dstack((a, b))
    print(res)

    import numpy as np

    arr = np.arange(14)
    res = np.array_split(arr, 4)
    print(res)

    import numpy as np

    arr1 = np.array([[1, 3], [4, 5]])
    arr2 = np.array([[1, 2], [3, 4]])

    dif = arr1 == arr2
    b = dif.all()
    print(b)

    import numpy as np

    a = np.array([10, 20, 30, 40])
    b = np.array([20, 50, 70, 80])

    res = np.union1d(a, b)
    print(res)

    import numpy as np

    a = np.array([[0, 0], [1, 1], [0, 0], [3, 2]])
    res = np.array(list({tuple(r) for r in a}))
    print(res)

