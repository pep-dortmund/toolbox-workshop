import numpy as np
from scipy.optimize import curve_fit
from scipy.signal import find_peaks
import matplotlib.pyplot as plt


def e(x, a, b, c):
    return a * np.exp(b * x) + c


t, U = np.genfromtxt("data.txt", unpack=True)
t *= 1e3

maxs, properties = find_peaks(U, prominence=1, distance=100)
mins, properties = find_peaks(-U, prominence=1, distance=100)

parameters_max, pcov_max = curve_fit(e, t[maxs], U[maxs])
print(parameters_max, np.sqrt(np.diag(pcov_max)), sep="\n")

parameters_min, pcov_min = curve_fit(e, t[mins], U[mins])
print(parameters_min, np.sqrt(np.diag(pcov_min)), sep="\n")

fig, ax = plt.subplots(1, 1, layout="constrained")

x = np.linspace(0, ax.get_xlim()[1], 500)

ax.plot(t, U, "k-", label="Gedämpfte Schwingung")

ax.plot(x, e(x, *parameters_max), label="Obere Einhüllende")
ax.plot(t[maxs], U[maxs], "o", color="C0", label="Maxima")

ax.plot(x, e(x, *parameters_min), label="Untere Einhüllende")
ax.plot(t[mins], U[mins], "o", color="C1", label="Minima")

ax.set_xlabel(r"$t \ / \ \mathrm{ms}$")
ax.set_ylabel(r"$U \ / \ \mathrm{V}$")
ax.set_xlim(0, 0.3)
ax.legend(loc="best")
fig.savefig("loesung.pdf")
