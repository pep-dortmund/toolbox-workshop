import numpy as np
import uncertainties.unumpy as unp


def linregress(x, y):
    N = len(y)  # Annahme: len(x) == len(y), sonst kommt während der Rechnung eine Fehlermeldung
    Delta = N * np.sum(x**2) - (np.sum(x))**2

    A = (N * np.sum(x * y) - np.sum(x) * np.sum(y)) / Delta
    B = (np.sum(x**2) * np.sum(y) - np.sum(x) * np.sum(x * y)) / Delta

    sigma_y = np.sqrt(np.sum((y - A * x - B)**2) / (N - 2))

    A_error = sigma_y * np.sqrt(N / Delta)
    B_error = sigma_y * np.sqrt(np.sum(x**2) / Delta)

    return A, A_error, B, B_error


def ulinregress(x, y):
    A, A_error, B, B_error = linregress(unp.nominal_values(x), unp.nominal_values(y))
    return unp.uarray([A, B], [A_error, B_error])
