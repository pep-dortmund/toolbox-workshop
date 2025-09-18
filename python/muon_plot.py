import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import correlated_values
import uncertainties.unumpy as unp

nom = unp.nominal_values
std = unp.std_devs


def decay_with_background(t, N0, lamb, back):
    return N0 * np.exp(-lamb * t) + back


def u_decay_with_background(t, N0, lamb, back):
    return N0 * unp.exp(-lamb * t) + back


N = np.genfromtxt("data/muon_data.txt")
N = N[5:-5]
N = N[::2]
t = (2 * np.arange(len(N)) + 5) / 21.48
N_err = np.sqrt(N)


params, cov = curve_fit(decay_with_background, t, N, p0=[400, 1, 5])
N0, Lamb, U = correlated_values(params, cov)

print("N0=", N0)
print("λ=", Lamb)
print("U=", U)
print("τ=", 1 / Lamb)

t_plot = np.linspace(0, 11, 1000)
y_plot = u_decay_with_background(t_plot, N0, Lamb, U)

fig, ax = plt.subplots(figsize=(15 / 2.54, 10 / 2.54), layout="constrained")

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
ax.plot(t_plot, nom(y_plot), "r-", label="Fit", lw=1)

ax.fill_between(
    t_plot,
    nom(y_plot) - 10 * std(y_plot),
    nom(y_plot) + 10 * std(y_plot),
    color="r",
    alpha=0.3,
    lw=0,
    label=r"$1\sigma$-Umgebung ($\times 10$)",
)

ax.set_title("Plot: matplotlib")

ax.annotate(
    "Messwerte einlesen: numpy",
    xy=(t[9], N[9]),
    xytext=(t[9] + 0.5, N[9] + 10),
)

ax.annotate(
    "Fit: scipy",
    xy=(t[50], N[50]),
    xytext=(t[50] + 0.5, N[50] + 30),
    color="r",
)

ax.annotate(
    "Fehlerrechnung: uncertainties",
    xy=(t[20], N[20]),
    xytext=(t[20] + 0.5, N[20] + 30),
    color="r",
    alpha=0.3,
)

ax.legend()
ax.set_xlabel(r"$t \mathbin{/} \unit{\micro\second}$")
ax.set_ylabel(r"Zählrate")
ax.set_xlim(0, 11)
ax.set_ylim(-50, 500)
fig.savefig("build/muon_plot.png", dpi=300)
