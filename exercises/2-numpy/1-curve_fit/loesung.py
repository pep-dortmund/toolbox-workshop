import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Datenfile erzeugen
from numpy.random import rand, randn
N = 50
data_x = np.linspace(0, 2 * np.pi, N)
data_y = np.sin(data_x)
error_y = 0.2 * rand(N) + 0.01
data_y += error_y * randn(N)
np.savetxt('daten.txt', np.array([data_x, data_y, error_y]).T, header='x y y_err')

x, y, e_y = np.loadtxt('daten.txt', unpack=True)

def f(x, a, b, c, d):
    return a * np.sin(b * x + c) + d

popt, pcov = curve_fit(f, x, y, sigma=e_y)
print(popt, np.sqrt(np.diag(pcov)), sep='\n')

plt.errorbar(x, y, yerr=e_y, fmt='rx', label='Daten')
t = np.linspace(-0.5, 2 * np.pi + 0.5)
plt.plot(t, f(t, *popt), 'b-', label='Fit')
plt.plot(t, np.sin(t), 'g--', label='Original')
plt.xlim(t[0], t[-1])
plt.xlabel(r'$t$')
plt.ylabel(r'$f(t)$')
plt.legend(loc='best')
plt.savefig('loesung.pdf')
