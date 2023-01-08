import matplotlib.pyplot as plt
import numpy as np








x = np.linspace(0, 10, 1000)
y = x ** np.sin(x)

plt.plot(x, y)
plt.xlabel(r"$\alpha \mathbin{/} \unit{\ohm}$")

plt.savefig("build/figures/mattex5.pdf", bbox_inches="tight", pad_inches=0)
