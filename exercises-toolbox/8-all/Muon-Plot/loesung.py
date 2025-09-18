import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import correlated_values
import uncertainties.unumpy as unp

noms = unp.nominal_values
stds = unp.std_devs

t = (2 * np.arange(110) + 5) / 21.48
# begin solution


def decay_with_background(t, N0, lamb, back):
    return N0 * np.exp(-lamb * t) + back


def u_decay_with_background(t, N0, lamb, back):
    return N0 * unp.exp(-lamb * t) + back


N = np.genfromtxt("muon_data.txt")
N = N[5:-5:2]
N_err = np.sqrt(N)

params, cov = curve_fit(decay_with_background, t, N, p0=[400, 1, 5])
N0, Lamb, U = correlated_values(params, cov)

print("N0=", N0)
print("λ=", Lamb)
print("U=", U)
print("τ=", 1 / Lamb)

t_plot = np.linspace(0, 11, 1000)
y_plot = u_decay_with_background(t_plot, N0, Lamb, U)

fig, ax = plt.subplots(layout="constrained")

ax.errorbar(
    t,
    N,
    yerr=N_err,
    xerr=np.diff(t)[0] / 2,
    color="k",
    label="Messwerte",
    ls="",
    lw=1,
)

ax.plot(t_plot, noms(y_plot), "r-", label="Fit", lw=1)

ax.fill_between(
    t_plot,
    noms(y_plot) - 10 * stds(y_plot),
    noms(y_plot) + 10 * stds(y_plot),
    color="r",
    alpha=0.3,
    lw=0,
    label=r"$1\sigma$-Umgebung ($\cdot 10$)",
)

ax.legend()
ax.set_xlabel(r"$t \mathbin{/} \unit{\micro\second}$")
ax.set_ylabel(r"Zählrate")
ax.set_xlim(0, 11)
ax.set_ylim(-25, 425)
ax.grid()
fig.savefig("build/loesung.pdf")

# end solution
