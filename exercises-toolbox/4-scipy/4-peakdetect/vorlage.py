import numpy as np
from scipy.optimize import curve_fit
from scipy.signal import find_peaks_cwt
import matplotlib.pyplot as plt

parameters_max = #

parameters_min = #

# Dieser Code erzeugt den Plot
fig, ax = plt.subplots(1, 1, layout="constrained")

ax.plot(t, U, "b-", label="Gedämpfte Schwingung")

ax.plot(t[maxs], U[maxs], "rx", label="Extrema")
ax.plot(x, e(x, *parameters_max), "g-", label="Obere Einhüllende")

ax.plot(t[mins], U[mins], "rx")
ax.plot(x, e(x, *parameters_min), "y-", label="Untere Einhüllende")

ax.set_xlabel(r"$t \ / \ \mathrm{ms}$")
ax.set_ylabel(r"$U \ / \ \mathrm{V}$")
ax.set_xlim(0, 0.3)
ax.legend(loc="best")
fig.savefig("loesung.pdf")
