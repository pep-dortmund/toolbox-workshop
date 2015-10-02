import numpy as np
from scipy.optimize import curve_fit
from scipy.signal import find_peaks_cwt
import matplotlib.pyplot as plt

t, U = np.loadtxt('data.txt', unpack=True)
t *= 1e3

plt.plot(t, U, 'b-', label='Gedämpfte Schwingung')

maxs = find_peaks_cwt(U, np.linspace(30, 50, 30))
mins = find_peaks_cwt(-U, np.linspace(30, 50, 30))

x = np.linspace(0, plt.xlim()[1])
def e(x, a, b, c):
    return a * np.exp(b * x) + c

popt, pcov = curve_fit(e, t[maxs], U[maxs])
print(popt, np.sqrt(np.diag(pcov)), sep='\n')
plt.plot(t[maxs], U[maxs], 'rx', label='Extrema')
plt.plot(x, e(x, *popt), 'g-', label='Obere Einhüllende')

popt, pcov = curve_fit(e, t[mins], U[mins])
print(popt, np.sqrt(np.diag(pcov)), sep='\n')
plt.plot(t[mins], U[mins], 'rx')
plt.plot(x, e(x, *popt), 'y-', label='Untere Einhüllende')

plt.xlabel(r'$t \ / \ \mathrm{ms}$')
plt.ylabel(r'$U \ / \ \mathrm{V}$')
plt.legend(loc='best')
plt.xlim(0, 0.3)
plt.tight_layout()
plt.savefig('loesung.pdf')
