import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

def f(x, a, b, c, d):
    # hier Funktion ergänzen

# hier Fit ergänzen
parameters = ?

# Dieser Code erstellt einen Plot mithilfe von f und parameters
fig, ax = plt.subplots(1, 1, layout="constrained")
ax.errorbar(x, y, yerr=e_y, fmt="rx", label="Daten")

t = np.linspace(-0.5, 2 * np.pi + 0.5)

ax.plot(t, f(t, *parameters), "b-", label="Fit")
ax.plot(t, np.sin(t), "g--", label="Original")
ax.set_xlim(t[0], t[-1])
ax.set_xlabel(r"$t$")
ax.set_ylabel(r"$f(t)$")
ax.legend(loc="best")
fig.savefig("loesung.pdf")
