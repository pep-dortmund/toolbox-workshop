

import matplotlib.pyplot as plt
import numpy as np








x = np.linspace(0, 10, 1000)
y = x ** np.sin(x)
plt.figure(figsize=(6.022, 3.39))                 # <-- set figure size
plt.plot(x, y)
plt.xlabel(r'$\alpha / \Omega$')

plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)   # <-- use tight_layout
plt.savefig('build/figures/mattex2.pdf')
