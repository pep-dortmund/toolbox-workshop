import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 100)

for n in range(1, 11):
    plt.plot(x, x**n, label='$x^{{{}}}$'.format(n))

plt.legend(loc='upper left')
plt.xlabel('$x$')
plt.tight_layout()
plt.savefig('loesung.pdf')
