

import matplotlib.pyplot as plt
import numpy as np








x = np.linspace(0, 10, 1000)
y = x ** np.sin(x)
# set figure size and use constrained_layout
fig = plt.figure(figsize=(6.022, 3.39), constrained_layout=True)
ax = fig.add_subplot(111)
ax.plot(x, y)
ax.set_xlabel(r'$\alpha / \Omega$')

fig.savefig('build/figures/mattex2.pdf', bbox_inches='tight', pad_inches=0)
