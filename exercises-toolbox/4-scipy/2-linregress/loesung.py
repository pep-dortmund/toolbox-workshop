import numpy as np


def linregress(x, y):
    # …
    # begin solution
    if not len(x) == len(y):
        raise ValueError("shape mismatch: x and y must have the same length")

    x, y = np.array(x), np.array(y)

    N = len(y)
    delta = N * np.sum(x**2) - (np.sum(x)) ** 2

    A = (N * np.sum(x * y) - np.sum(x) * np.sum(y)) / delta
    B = (np.sum(x**2) * np.sum(y) - np.sum(x) * np.sum(x * y)) / delta

    sigma_y = np.sqrt(np.sum((y - A * x - B) ** 2) / (N - 2))

    A_error = sigma_y * np.sqrt(N / delta)
    B_error = sigma_y * np.sqrt(np.sum(x**2) / delta)

    # end solution
    return A, A_error, B, B_error


# begin solution

if __name__ == "__main__":
    x, y = np.genfromtxt("data.txt", unpack=True)
    print(linregress(x, y))
# end solution
