

import matplotlib.pyplot as plt
import numpy as np








x = np.linspace(0, 10, 1000)
y = x ** np.sin(x)

fig, ax = plt.subplots(layout="constrained")

ax.plot(x, y)
ax.set_xlabel(r"$\alpha / \Omega$")

fig.savefig("build/figures/mattex1.pdf")
