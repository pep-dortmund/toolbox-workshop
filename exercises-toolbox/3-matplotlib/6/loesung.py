import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 100)

fig, ax = plt.subplots(1, 1, layout="constrained")

for n in range(1, 11):
    ax.plot(x, x ** n, label=f"$x^{{{n}}}$")

ax.legend(loc="upper left")
ax.set_xlabel("$x$")
fig.savefig("loesung.pdf")
