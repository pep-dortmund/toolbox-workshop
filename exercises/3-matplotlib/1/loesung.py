import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 1)

plt.plot(x, x**2, 'b-')
plt.xlabel(r'$x$')
plt.ylabel(r'$x^2$')
plt.savefig('1.pdf')
