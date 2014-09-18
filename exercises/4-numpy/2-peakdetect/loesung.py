# encoding: utf-8
from __future__ import (print_function,
                        division,
                        unicode_literals,
                        absolute_import)

import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

import peakdetect

t, U = np.loadtxt('data.txt', unpack=True)
t *= 1e3

plt.plot(t, U, 'b-', label='Gedämpfte Schwingung')

maxs, mins = peakdetect.peakdetect(U, t, 4, 1)
maxs = np.array(maxs).T
mins = np.array(mins).T

x = np.linspace(0, plt.xlim()[1])

def e(x, a, b, c):
    return a * np.exp(b * x) + c

popt, pcov = curve_fit(e, maxs[0], maxs[1])
print(popt, np.sqrt(np.diag(pcov)), sep='\n')
plt.plot(maxs[0], maxs[1], 'rx', label='Extrema')
plt.plot(x, e(x, *popt), 'g-', label='Obere Einhüllende')

popt, pcov = curve_fit(e, mins[0], mins[1])
print(popt, np.sqrt(np.diag(pcov)), sep='\n')
plt.plot(mins[0], mins[1], 'rx')
plt.plot(x, e(x, *popt), 'y-', label='Untere Einhüllende')

plt.xlabel(r'$t \,\, / \,\, \mathrm{ms}$')
plt.ylabel(r'$U \,\, / \,\, \mathrm{V}$')
plt.legend(loc='best')
plt.xlim(0, 0.3)
plt.savefig('loesung.pdf')
