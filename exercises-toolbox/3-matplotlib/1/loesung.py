import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 1)

plt.figure(constrained_layout=True)

plt.plot(x, x ** 2)

plt.xlabel(r"$x$")
plt.ylabel(r"$x^2$")

plt.savefig("loesung.pdf")
