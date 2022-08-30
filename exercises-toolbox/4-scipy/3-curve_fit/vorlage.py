import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

def f(x, a, b, c, d):
    # hier Funktion ergänzen

# hier Fit ergänzen
parameters = ?

# Dieser Code erstellt einen Plot mithilfe von f und parameters
plt.figure(constrained_layout=True)
plt.errorbar(x, y, yerr=e_y, fmt='rx', label='Daten')
t = np.linspace(-0.5, 2 * np.pi + 0.5)
plt.plot(t, f(t, *parameters), 'b-', label='Fit')
plt.plot(t, np.sin(t), 'g--', label='Original')
plt.xlim(t[0], t[-1])
plt.xlabel(r'$t$')
plt.ylabel(r'$f(t)$')
plt.legend(loc='best')
plt.savefig('loesung.pdf')
