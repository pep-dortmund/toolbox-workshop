import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt


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

parameters, pcov = curve_fit(
    theory,
    phi,
    I,
    p0=[np.sqrt(np.max(I)) / 1e-4, 1e-4],
)
print(parameters, np.sqrt(np.diag(pcov)), sep="\n")

x = np.linspace(-0.03, 0.03, 100)

fig, ax = plt.subplots(1, 1, layout="constrained")

ax.plot(x, theory(x, *parameters), "-", label="Fit")
ax.plot(phi, I, "k.", label="Daten")

ax.set_xlabel(r"$\varphi \ / \ \mathrm{rad}$")
ax.set_ylabel(r"$I \ / \ \mathrm{A}$")
ax.legend(loc="best")

fig.savefig("loesung.pdf")
