import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

def theory(phi, A0, b):
    # Hier Funktion ergänzen

# Hier Fit ergänzen
parameters = ?

# Hier wird der Plot erstellt
x = np.linspace(-0.03, 0.03, 100)
plt.plot(x, theory(x, *parameters), 'b-', label='Fit')
plt.plot(phi, I, 'rx', label='Daten')
plt.xlabel(r'$\varphi \ / \ \mathrm{rad}$')
plt.ylabel(r'$I \ / \ \mathrm{A}$')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('loesung.pdf')
