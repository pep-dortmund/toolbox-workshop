import matplotlib.pyplot as plt
import numpy as np








x = np.linspace(0, 10, 1000)
y = x ** np.sin(x)

fig, ax = plt.subplots(1, 1, layout="constrained")
ax.plot(x, y)
ax.set_xlabel(r"$\alpha \mathbin{/} \unit{\ohm}$")

fig.savefig("build/figures/mattex5.pdf", bbox_inches="tight", pad_inches=0)
