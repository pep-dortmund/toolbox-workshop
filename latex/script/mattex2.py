

import matplotlib.pyplot as plt
import numpy as np








x = np.linspace(0, 10, 1000)
y = x ** np.sin(x)
# set figure size and use constrained_layout
plt.figure(figsize=(6.022, 3.39), constrained_layout=True)
plt.plot(x, y)
plt.xlabel(r'$\alpha / \Omega$')

plt.savefig('build/figures/mattex2.pdf', bbox_inches='tight', pad_inches=0)
