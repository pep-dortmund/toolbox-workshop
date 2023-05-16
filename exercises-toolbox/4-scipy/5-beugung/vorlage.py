import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt


def theory(phi, A0, b):
    '''Hier Funktion ergänzen'''


# Hier Fit ergänzen
parameters, cov = #

# Hier wird der Plot erstellt
x = np.linspace(-0.03, 0.03, 100)

plt.figure(layout="constrained")

plt.plot(x, theory(x, *parameters), '-', label='Fit')
plt.plot(phi, I, 'k.', label='Daten')

plt.xlabel(r'$\varphi \ / \ \mathrm{rad}$')
plt.ylabel(r'$I \ / \ \mathrm{A}$')
plt.legend()

plt.savefig('loesung.pdf')
