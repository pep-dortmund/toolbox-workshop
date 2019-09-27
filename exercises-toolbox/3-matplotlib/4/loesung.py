import matplotlib.pyplot as plt
import numpy as np

# Datenfile erzeugen
np.random.seed(0)
N = 20
error_x = np.random.lognormal(-2, 0.05, size=N)
data_x = np.random.normal(np.linspace(0, 2 * np.pi, N), error_x)
error_y = np.random.lognormal(-1.2, 0.3, size=N)
data_y = np.random.normal(np.sin(data_x), error_y)
np.savetxt(
    '4.txt',
    np.column_stack([data_x, error_x, data_y, error_y]),
    header='x err_x y err_y',
)

x, e_x, y, e_y = np.genfromtxt('4.txt', unpack=True)

t = np.linspace(-0.5, 2 * np.pi + 0.5)

plt.errorbar(x, y, xerr=e_x, yerr=e_y, fmt='k.', label='Daten')
plt.plot(t, np.sin(t), label=r'$\sin(t)$')

plt.xlim(t[0], t[-1])
plt.xlabel(r'$t$')
plt.ylabel(r'$f(t)$')

plt.legend()
plt.tight_layout()
plt.savefig('loesung.pdf')
