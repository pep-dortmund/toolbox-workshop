import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi)

plt.plot(x, np.sin(x), 'r-', label=r'$\sin(x)$')
plt.plot(x, np.cos(x), 'b--', label=r'$\cos(x)$')
plt.xlim(0, 2 * np.pi)
plt.ylim(-1.2, 1.2)
plt.xlabel(r'$x$')
plt.xticks(np.arange(0, 2.1*np.pi, np.pi/2), ['$0$', r'$\frac{\pi}{2}$', r'$\pi$', r'$\frac{3\pi}{2}$', r'$2\pi$'])
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('5.pdf', bbox_inches='tight', pad_inches=0)
