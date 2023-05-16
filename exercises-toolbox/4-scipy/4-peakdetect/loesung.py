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

x = np.linspace(0, plt.xlim()[1], 500)

parameters_max, pcov_max = curve_fit(e, t[maxs], U[maxs])
print(parameters_max, np.sqrt(np.diag(pcov_max)), sep="\n")

parameters_min, pcov_min = curve_fit(e, t[mins], U[mins])
print(parameters_min, np.sqrt(np.diag(pcov_min)), sep="\n")

plt.figure(layout="constrained")

plt.plot(t, U, "k-", label="Gedämpfte Schwingung")

plt.plot(x, e(x, *parameters_max), label="Obere Einhüllende")
plt.plot(t[maxs], U[maxs], "o", color="C0", label="Maxima")

plt.plot(x, e(x, *parameters_min), label="Untere Einhüllende")
plt.plot(t[mins], U[mins], "o", color="C1", label="Minima")

plt.xlabel(r"$t \ / \ \mathrm{ms}$")
plt.ylabel(r"$U \ / \ \mathrm{V}$")
plt.legend()
plt.xlim(0, 0.3)
plt.savefig("loesung.pdf")
