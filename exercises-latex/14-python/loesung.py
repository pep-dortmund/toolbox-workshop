import matplotlib as mpl
mpl.rcdefaults()
mpl.rcParams.update(mpl.rc_params_from_file('loesung-matplotlibrc'))
import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from uncertainties.unumpy import (
    nominal_values as noms,
    std_devs as stds,
)

from curve_fit import ucurve_fit
from table import (
    make_table,
    make_SI,
    write,
)

t, U, U_err = np.genfromtxt('data.txt', unpack=True)
t *= 1e-3
U = 1e3 * unp.uarray(U, U_err)

def f(t, a, b, c, d):
    return a * np.sin(b * t + c) + d

params = ucurve_fit(f, t, U, p0=[1, 1e3, 0, 0])

t_plot = np.linspace(-0.5, 2 * np.pi + 0.5, 1000) * 1e-3
plt.plot(t_plot * 1e3, f(t_plot, *noms(params)) * 1e-3, 'b-', label='Fit')
plt.errorbar(t * 1e3, noms(U) * 1e-3, yerr=stds(U) * 1e-3, fmt='r_', label='Daten')
plt.xlim(t_plot[0] * 1e3, t_plot[-1] * 1e3)
plt.xlabel(r'$t \:/\: \si{\milli\second}$')
plt.ylabel(r'$U \:/\: \si{\kilo\volt}$')
plt.legend(loc='best')
plt.savefig('build/loesung-plot.pdf')

t1, t2 = np.array_split(t * 1e3, 2)
U1, U2 = np.array_split(U * 1e-3, 2)
write('build/loesung-table.tex', make_table([t1, U1, t2, U2], [3, None, 3, None]))

a, b, c, d = params
write('build/loesung-a.tex', make_SI(a * 1e-3, r'\kilo\volt'))
write('build/loesung-b.tex', make_SI(b * 1e-3, r'\kilo\hertz'))
write('build/loesung-c.tex', make_SI(c,        r''))
write('build/loesung-d.tex', make_SI(d * 1e-3, r'\kilo\volt'))
