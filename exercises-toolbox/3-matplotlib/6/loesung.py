import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 100)

plt.figure(layout="constrained")

for n in range(1, 11):
    plt.plot(x, x ** n, label=f"$x^{{{n}}}$")

plt.legend(loc="upper left")
plt.xlabel("$x$")
plt.savefig("loesung.pdf")
