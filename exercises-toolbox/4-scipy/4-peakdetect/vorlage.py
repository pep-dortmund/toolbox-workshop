import numpy as np
from scipy.optimize import curve_fit
from scipy.signal import find_peaks_cwt
import matplotlib.pyplot as plt

parameters_max = #

parameters_min = #

# Dieser Code erzeugt den Plot
plt.figure(constrained_layout=True)

plt.plot(t, U, 'b-', label='Gedämpfte Schwingung')

plt.plot(t[maxs], U[maxs], 'rx', label='Extrema')
plt.plot(x, e(x, *parameters_max), 'g-', label='Obere Einhüllende')

plt.plot(t[mins], U[mins], 'rx')
plt.plot(x, e(x, *parameters_min), 'y-', label='Untere Einhüllende')

plt.xlabel(r'$t \ / \ \mathrm{ms}$')
plt.ylabel(r'$U \ / \ \mathrm{V}$')
plt.legend(loc='best')
plt.xlim(0, 0.3)
plt.savefig('loesung.pdf')
