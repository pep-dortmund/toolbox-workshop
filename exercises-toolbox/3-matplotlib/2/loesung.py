import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 1)

plt.plot(x, x**2, 'b-', label=r'$x^2$')
plt.plot(x, x**5, 'gx', label=r'$x^5$')
plt.xlabel(r'$x$')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('loesung.pdf')
