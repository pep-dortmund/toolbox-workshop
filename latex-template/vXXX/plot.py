import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 1000)
y = x ** np.sin(x)

plt.figure(layout="constrained")

plt.subplot(1, 2, 1)
plt.plot(x, y, label="Kurve")
plt.xlabel(r"$\alpha \mathbin{/} \unit{\ohm}$")
plt.ylabel(r"$y \mathbin{/} \unit{\micro\joule}$")
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(x, y, label="Kurve")
plt.xlabel(r"$\alpha \mathbin{/} \unit{\ohm}$")
plt.ylabel(r"$y \mathbin{/} \unit{\micro\joule}$")
plt.legend()

plt.savefig("build/plot.pdf")
