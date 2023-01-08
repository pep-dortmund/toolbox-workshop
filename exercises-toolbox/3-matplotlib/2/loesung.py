import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 1)

plt.figure(layout="constrained")

plt.plot(x, x**2, label=r"$x^2$")
plt.plot(x, x**5, "x", label=r"$x^5$")

plt.legend(loc="best")
plt.xlabel(r"$x$")

plt.savefig("loesung.pdf")
