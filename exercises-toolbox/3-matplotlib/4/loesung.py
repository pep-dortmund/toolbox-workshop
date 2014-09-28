import matplotlib.pyplot as plt
import numpy as np
from numpy.random import randn
from scipy.optimize import curve_fit

def f(x, a, b, c):
    return a*np.sin(b*x) +c

# Datenfile erzeugen
data_x = np.linspace(0, 2 * np.pi, 50)
data_y = np.sin(data_x)
data_x += 0.1 * randn(50)
data_y += 0.2 * randn(50)
error_x = 0.1 * 0.5 * randn(50)
error_y = 0.2 * 0.5 * randn(50)
np.savetxt('4.txt', np.array([data_x, error_x, data_y, error_y]).T)

x, e_x, y, e_y = np.genfromtxt('4.txt', unpack=True)

plt.errorbar(x, y, xerr=e_x, yerr=e_y, fmt='rx', label='Daten')

t = np.linspace(-0.5, 2 * np.pi + 0.5)

params, cov = curve_fit(f, x, y, sigma=e_y)

print(params)

plt.plot(t, f(t, *params), 'b-', label='Fit')

plt.xlim(t[0], t[-1])
plt.xlabel(r'$t$')
plt.ylabel(r'$f(t)$')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('loesung.pdf')
