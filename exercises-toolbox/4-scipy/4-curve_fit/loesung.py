import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# begin solution
# Datenfile erzeugen
rng = np.random.default_rng(42)

N = 50
data_x = np.linspace(0, 2 * np.pi, N)
error_y = rng.lognormal(-1, 0.2, size=N)
data_y = rng.normal(np.sin(data_x), error_y)

np.savetxt("daten.txt", np.column_stack([data_x, data_y, error_y]), header="x y y_err")

# Ab hier beginnt die Lösung
x, y, e_y = np.genfromtxt("daten.txt", unpack=True)

# end solution


def f(x, a, b, c, d):
    # hier Funktion ergänzen
    # begin solution
    return a * np.sin(b * x + c) + d
    # end solution


# hier Fit ergänzen
# parameters = ?
# begin solution
parameters, pcov = curve_fit(f, x, y, sigma=e_y)
print(parameters, np.sqrt(np.diag(pcov)), sep="\n")

# end solution
# Dieser Code erstellt einen Plot mithilfe von f und parameters
fig, ax = plt.subplots(1, 1, layout="constrained")
ax.errorbar(x, y, yerr=e_y, fmt="k.", label="Daten")

t = np.linspace(-0.5, 2 * np.pi + 0.5, 500)

ax.plot(t, f(t, *parameters), "b-", label="Fit")
ax.plot(t, np.sin(t), "g--", label="Original")

ax.set_xlim(t[0], t[-1])
ax.set_xlabel(r"$t$")
ax.set_ylabel(r"$f(t)$")
ax.legend()

fig.savefig("loesung.pdf")
