import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat, correlated_values


def decay_with_background(t, N0, lamb, back):
    return N0 * np.exp(-lamb*t) + back

N = np.genfromtxt("./muon_data.txt")
N = np.delete(N, [0,1,2,3, -1, -2, -3, -4, -5, -6])
t = (np.arange(len(N)) + 5)/21.48
N_err = np.sqrt(N)

t_plot = np.linspace(0, max(t), 1000)

params, cov = curve_fit(decay_with_background, t, N, p0=[400, 1, 5])

N0, Lamb, U = correlated_values(params, cov)

print("N0=", N0)
print("λ=", Lamb)
print("U=", U)

print("τ=", 1/Lamb)


fig = plt.figure(figsize=(15/2.54, 10/2.54))
ax = fig.add_subplot(1,1,1)

ax.errorbar(t, N, yerr=N_err, fmt='k+', label="Messwerte")
ax.plot(t_plot, decay_with_background(t_plot, *params), 'r-', label="Fit")

ax.legend(loc="best")
ax.set_xlabel(r"$t/\si{\micro\second}$")
ax.set_ylabel(r"Zählrate")
fig.tight_layout()
fig.savefig("muon_plot.png", dpi=100)
