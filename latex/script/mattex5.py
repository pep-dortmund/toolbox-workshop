



import matplotlib.pyplot as plt
import numpy as np








x = np.linspace(0, 10, 1000)
y = x ** np.sin(x)

plt.plot(x, y)
plt.xlabel(r'$\alpha / \si{\ohm}$')
# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/figures/mattex5.pdf')
