import matplotlib as mpl
mpl.rcdefaults()


import matplotlib.pyplot as plt
import numpy as np







x = np.linspace(0, 10, 1000)
y = x ** np.sin(x)

plt.plot(x, y)
plt.xlabel(r'$\alpha / \Omega$')


plt.savefig('build/figures/mattex1.pdf')

