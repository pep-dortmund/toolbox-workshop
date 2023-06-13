import numpy as np
import uncertainties as unc
import uncertainties.unumpy as unp
from uncertainties.unumpy import nominal_values as noms, std_devs as stds
import matplotlib.pyplot as plt

from linregress import ulinregress

Delta_t_0 = np.genfromtxt("Delta_t_0.txt")
N_0 = np.genfromtxt("N_0.txt")
N_0 = unc.ufloat(N_0, np.sqrt(N_0))

Delta_t = np.genfromtxt("Delta_t.txt")
N_g = np.genfromtxt("N_g.txt", unpack=True)
N_g = unp.uarray(N_g, np.sqrt(N_g))

t = Delta_t * np.arange(1, len(N_g) + 1)
N = N_g - N_0 / Delta_t_0 * Delta_t

A, B = ulinregress(t, unp.log(N))
print(A, B, sep="\n")
lambda_ = -A
print("λ =", lambda_)

x = np.linspace(0, 4000)
fig, ax = plt.subplots(1, 1, layout="constrained")
ax.plot(x, np.exp(noms(A * x + B)), label="Regressionsgerade")
ax.errorbar(t, noms(N), yerr=stds(N), fmt="x", label="Messwerte")
ax.set_yscale("log", nonpositive="clip")
ax.set_xlabel(r"$t \,/\, \mathrm{s}$")
ax.set_ylabel(r"$N$")
ax.set_ylim(8e2, 3e3)
ax.set_yticks([8e2, 1e3, 3e3], [r"$8 \cdot 10^2$", r"$10^3$", r"$3 \cdot 10^3$"])
ax.legend(loc="upper right")
fig.savefig("loesung.pdf")
