import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt


def theory(phi, A0, b):
    """Hier Funktion ergänzen"""


# Hier Fit ergänzen
parameters, cov = #

# Hier wird der Plot erstellt
x = np.linspace(-0.03, 0.03, 100)

fig, ax = plt.subplots(1, 1, layout="constrained")

ax.plot(x, theory(x, *parameters), "-", label="Fit")
ax.plot(phi, I, "k.", label="Daten")

ax.set_xlabel(r"$\varphi \ / \ \mathrm{rad}$")
ax.set_ylabel(r"$I \ / \ \mathrm{A}$")
ax.legend(loc="best")

fig.savefig("loesung.pdf")
