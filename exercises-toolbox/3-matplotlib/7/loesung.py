# begin solution
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 100)

fig, ax = plt.subplots(1, 1, layout="constrained")

for A in (-1, -0.5, 0.5, 1):
    ax.plot(x, A * np.cos(x), label=f"$A = {A}$")

ax.legend()
ax.set_xlim(0, 2 * np.pi)
ax.set_xlabel("$x$")
ax.set_ylabel(r"$A \cos(x)$")
fig.savefig("loesung.pdf")
# end solution
