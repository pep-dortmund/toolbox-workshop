# begin solution
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 1)

fig, ax = plt.subplots(1, 1, layout="constrained")

ax.plot(x, x**2, label=r"$x^2$")
ax.plot(x, x**5, "x", label=r"$x^5$")

ax.legend(loc="best")
ax.set_xlabel(r"$x$")

fig.savefig("loesung.pdf")
# end solution
