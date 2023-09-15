import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import correlated_values


def theory(phi, A0, b):
    return (A0 * b * np.sinc(b * np.sin(phi) / lambda_)) ** 2


L = np.genfromtxt("L.txt")
L *= 1e-2
lambda_ = np.genfromtxt("lambda.txt")
lambda_ *= 1e-9
zeta, I = np.genfromtxt("I.txt", unpack=True)
zeta *= 1e-3
I *= 1e-9

zeta_0 = zeta[np.argmax(I)]
phi = (zeta - zeta_0) / L

params, cov = curve_fit(theory, phi, I, p0=[np.sqrt(np.max(I)) / 1e-4, 1e-4])

A0, b = correlated_values(params, cov)

print("A0 =", A0)
print("b =", b)

x = np.linspace(-0.03, 0.03, 100)

fig, ax = plt.subplots(1, 1, layout="constrained")
ax.plot(x, theory(x, *params), label="Fit")
ax.plot(phi, I, "x", label="Daten")
ax.set_xlabel(r"$\varphi \,\, / \,\, \mathrm{rad}$")
ax.set_ylabel(r"$I \,\, / \,\, \mathrm{A}$")
ax.legend(loc="best")
fig.savefig("loesung.pdf")