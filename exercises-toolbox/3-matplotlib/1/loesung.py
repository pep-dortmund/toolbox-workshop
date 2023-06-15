import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 1)

fig, ax = plt.subplots(1, 1, layout="constrained")

ax.plot(x, x**2)

ax.set_xlabel(r"$x$")
ax.set_ylabel(r"$x^2$")

fig.savefig("loesung.pdf")
