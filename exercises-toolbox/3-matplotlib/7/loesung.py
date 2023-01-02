import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 100)

plt.figure(layout="constrained")

for A in (-1, -0.5, 0.5, 1):
    plt.plot(x, A * np.cos(x), label=f"$A = {A}$")

plt.legend()
plt.xlim(0, 2 * np.pi)
plt.xlabel("$x$")
plt.ylabel(r"$A \cos(x)$")
plt.savefig("loesung.pdf")
