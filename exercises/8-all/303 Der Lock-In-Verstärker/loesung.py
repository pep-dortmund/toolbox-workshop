# encoding: utf-8
from __future__ import (print_function,
                        division,
                        unicode_literals,
                        absolute_import)

import numpy as np
import uncertainties as unc
import uncertainties.unumpy as unp
from uncertainties.unumpy import (nominal_values as noms,
                                  std_devs as stds)
import matplotlib as mpl
import matplotlib.pyplot as plt

from curve_fit import ucurve_fit

r, U, PA, LI, LP = np.loadtxt('LED', unpack=True)
r *= 1e-2
U /= PA * LI * LP

def Ur(r, A, B, C):
  return A + B / (r + C)**2

A, B, C = ucurve_fit(Ur, r, U)
print(A, B, C, sep='\n')

x = np.linspace(r[0] - 0.002, 1.6, 1000)
plt.plot(x, noms(Ur(x, A, B, C)), 'b-', label='Ausgleichskurve')
plt.plot(r, U, 'rx', label='Messwerte')
plt.xlim(0, 1.6)
plt.ylim(-0.05, 0.3)
plt.xlabel(r'$r \,/\, \mathrm{m}$')
plt.ylabel(r'$U \,/\, \mathrm{V}$')
plt.legend(loc='upper right')
plt.tight_layout()
plt.savefig('loesung.pdf')
