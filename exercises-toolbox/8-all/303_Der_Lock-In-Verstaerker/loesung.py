import numpy as np
from uncertainties.unumpy import nominal_values as noms
import matplotlib.pyplot as plt

from curve_fit import ucurve_fit


def Ur(r, A, B, C):
    return A + B / (r + C) ** 2


r, U, PA, LI, LP = np.genfromtxt("LED.txt", unpack=True)
r *= 1e-2
U /= PA * LI * LP

A, B, C = ucurve_fit(Ur, r, U)
print(A, B, C, sep="\n")

x = np.linspace(r[0] - 0.002, 1.6, 1000)
plt.figure(constrained_layout=True)
plt.plot(x, noms(Ur(x, A, B, C)), label="Ausgleichskurve")
plt.plot(r, U, "x", label="Messwerte")
plt.xlim(0, 1.6)
plt.ylim(-0.05, 0.3)
plt.xlabel(r"$r \,/\, \mathrm{m}$")
plt.ylabel(r"$U \,/\, \mathrm{V}$")
plt.legend(loc="upper right")
plt.savefig("loesung.pdf")
