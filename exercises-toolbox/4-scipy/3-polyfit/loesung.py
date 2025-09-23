# begin solution
import numpy as np
import matplotlib.pyplot as plt

# Generate data
rng = np.random.default_rng(210)

N = 50
data_x = np.linspace(-10, 10, N)
error_y = rng.lognormal(-1, 0.2, size=N)
data_y = rng.normal(data_x**2, error_y)

np.savetxt("daten.txt", np.column_stack([data_x, data_y, error_y]), header="x y y_err")

# Hier Fit hinzufügen
# The solution starts here
x, y, e_y = np.genfromtxt("daten.txt", unpack=True)


def f(x, a, b, c):
    return a * (x + b) ** 2 + c


parameters, covariance_matrix = np.polyfit(x, y, deg=2, cov=True)
uncertainties = np.sqrt(np.diag(covariance_matrix))

for name, value, unc in zip("abc", parameters, uncertainties):
    print(f"{name} = {value:.3f} ± {unc:.3f}")

# end solution


# Dieser Code erstellt einen Plot mithilfe von f und parameters
fig = plt.figure(layout="constrained")
ax = fig.add_subplot()

ax.errorbar(x, y, yerr=e_y, fmt="k.", label="data")

t = np.linspace(-10, 10, 500)
ax.plot(t, f(t, *parameters), label="Fit")
ax.plot(t, t**2, "--", label="Original")

ax.set_xlim(t[0], t[-1])
ax.set_xlabel(r"$t$")
ax.set_ylabel(r"$f(t)$")
ax.legend()

plt.savefig("loesung.pdf")
# end solution
