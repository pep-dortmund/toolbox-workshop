import matplotlib.pyplot as plt
import numpy as np

# Datenfile erzeugen
data_x = np.linspace(0, 10, 100)
data_y = 10 * np.exp(-data_x)
np.savetxt('3.txt', np.column_stack([data_x, data_y]), header='x y')

x, y = np.genfromtxt('3.txt', unpack=True)

plt.subplot(1, 2, 1)
plt.plot(x, y, 'rx')
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')
plt.subplot(1, 2, 2)
plt.plot(x, y, 'rx')
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')
plt.yscale('log')
plt.tight_layout()
plt.savefig('loesung.pdf')
