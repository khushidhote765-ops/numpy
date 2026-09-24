import numpy as np


def gaussian_filter(kernel_size, sigma=1, muu=0):
    # Initializing value of x, y as grid of kernel size in the range of kernel size
    x, y = np.meshgrid(np.linspace(-2, 2, kernel_size),
                       np.linspace(-2, 2, kernel_size))
    dst = np.sqrt(x ** 2 + y ** 2)

    # Normal part of the Gaussian function
    normal = 1 / (2 * np.pi * sigma ** 2)

    # Calculating Gaussian filter
    gauss = np.exp(-((dst - muu) ** 2 / (2.0 * sigma ** 4))) * normal

    return gauss  # Return the calculated Gaussian filter


# Example usage:
kernel_size = 4
gaussian = gaussian_filter(kernel_size=kernel_size)
print("Gaussian filter of {} X {}:".format(kernel_size, kernel_size))
print(gaussian)

import numpy as np

list1 = [6, 7, 8]

vector = np.array(list1)
print("Vector  : " + str(vector))

scalar = 2
print("Scalar  : " + str(scalar))

scalar_mul = vector * scalar
print("Scalar Multiplication : " + str(scalar_mul))