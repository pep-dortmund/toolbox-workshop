



import matplotlib.pyplot as plt
import numpy as np








x = np.linspace(0, 10, 1000)
y = x ** np.sin(x)

plt.plot(x, y)
plt.xlabel(r'$\alpha / \si{\ohm}$')
plt.tight_layout(pad=0)  # pad=0 in matplotlibrc leider nicht möglich
plt.savefig('build/figures/mattex5.pdf')

