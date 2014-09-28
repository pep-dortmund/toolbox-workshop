import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

L, C, R = np.loadtxt('geraetedaten.txt', unpack=True)
L *= 1e-3
C *= 1e-9

nu, arg, Z = np.loadtxt('impedanz.txt', unpack=True)
nu *= 1e3
omega = 2 * np.pi * nu
arg = np.deg2rad(arg)

x = np.linspace(150e3, 350e3, 1000)
Z_theor = np.sqrt(R**2 + (L * x - 1 / (C * x))**2)

plt.plot(x, Z_theor, 'b-', label='Theoriekurve')
plt.plot(omega, Z, 'rx', label='Messwerte')
plt.yscale('log')
plt.xlabel(r'$\omega \,/\, \mathrm{kHz}$')
plt.ylabel(r'$|Z| \,/\, \mathrm{\Omega}$')
plt.ylim(20, 1e3)
plt.gca().xaxis.set_major_formatter(mpl.ticker.FuncFormatter(lambda x, _: int(x * 1e-3)))
plt.legend(loc='lower right')
plt.tight_layout()
plt.savefig('loesung-log.pdf')

plt.clf()

x = np.linspace(2 * np.pi * 27e1, 2 * np.pi * 50e4, 1000)
phi1 = np.arctan(1 / R * (L * x - 1 / (C * x)))
phi2 = -phi1
Z_theor = np.sqrt(R**2 + (L * x - 1 / (C * x))**2)

plt.polar(phi1, Z_theor,'b', label='Theoriekurve')
plt.polar(phi2, Z_theor, 'b')
plt.polar(arg, Z, 'rx', label='Messwerte')
plt.ylim(0, 600)
plt.xlabel(r'$\varphi \,/\, \mathrm{rad}$')
plt.figtext(0.67, 0.68, r'$|Z| \,/\, \mathrm{\Omega}$')
plt.thetagrids([0, 45, 90, 135, 180, 225, 270, 315], labels=[r'$0$',
                                                             r'$\frac{1}{4} \pi$',
                                                             r'$\frac{1}{2} \pi$',
                                                             r'$\frac{3}{4} \pi$',
                                                             r'$\pm \pi$',
                                                             r'$- \frac{3}{4} \pi$',
                                                             r'$- \frac{1}{2} \pi$',
                                                             r'$- \frac{1}{4} \pi$'])
plt.rgrids([200, 400, 600])
plt.legend(bbox_to_anchor=(0.45, 0.8, 0, 0))
plt.tight_layout()
plt.savefig('loesung-polar.pdf')
