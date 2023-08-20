import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize
import uncertainties as unc
import uncertainties.unumpy as unp


def ucurve_fit(f, x, y, **kwargs):
    if np.any(unp.std_devs(y) == 0):
        sigma = None
    else:
        sigma = unp.std_devs(y)

    popt, pcov = scipy.optimize.curve_fit(
        f, x, unp.nominal_values(y), sigma=sigma, absolute_sigma=True, **kwargs
    )

    return unc.correlated_values(popt, pcov)


def f(x, a, b, c):
    return a * np.cos(x * b) + c

# Generate data
length = 100
x = np.linspace(0, 3 * np.pi, length)
rng = np.random.default_rng()
y1 = rng.normal(0.0, 0.2, length)
y2 = np.abs(rng.normal(0.0, 0.2, length))

y = f(x, 1, 1, -3) + y1

np.savetxt("daten.txt", np.column_stack([x, y, y2]), header="x\ty\ty_err")

# Solution
x, y_0, y_err = np.genfromtxt("daten.txt", unpack=True)
y = unp.uarray(y_0, y_err)
params = ucurve_fit(f, x, y)
print("a * cos(x * b) + c")
for char, p in zip("abc", params):
    print(f"{char} = {p}")

fig = plt.figure(layout="constrained")
ax = fig.add_subplot()
ax.errorbar(x, unp.nominal_values(y), yerr=y_err, fmt=".", label="Daten")
ax.plot(x, f(x, *unp.nominal_values(params)), label="Fit")
ax.set_xticks([0, np.pi, 2 * np.pi, 3 * np.pi], [0, "π", "2π", "3π"])
ax.legend()
plt.savefig("loesung.pdf")
