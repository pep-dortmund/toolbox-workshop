# begin solution
import numpy as np
import matplotlib.pyplot as plt

L, C, R = np.genfromtxt("geraetedaten.txt", unpack=True)
L *= 1e-3
C *= 1e-9

nu, arg, Z = np.genfromtxt("impedanz.txt", unpack=True)
nu *= 1e3
omega = 2 * np.pi * nu
arg = np.deg2rad(arg)

x = np.linspace(150e3, 350e3, 1000)
Z_theor = np.sqrt(R**2 + (L * x - 1 / (C * x)) ** 2)

fig, ax = plt.subplots(1, 1, layout="constrained")
ax.plot(x * 1e-3, Z_theor, label="Theoriekurve")
ax.plot(omega * 1e-3, Z, "x", label="Messwerte")
ax.set_yscale("log")
ax.set_xlabel(r"$\omega \,/\, \mathrm{kHz}$")
ax.set_ylabel(r"$|Z| \,/\, \mathrm{\Omega}$")
ax.set_ylim(20, 1e3)
ax.legend(loc="lower right")
fig.savefig("loesung-log.pdf")
fig.clf()

x = np.linspace(2 * np.pi * 27e1, 2 * np.pi * 50e4, 1000)
phi1 = np.arctan(1 / R * (L * x - 1 / (C * x)))
phi2 = -phi1
Z_theor = np.sqrt(R**2 + (L * x - 1 / (C * x)) ** 2)

fig, ax = plt.subplots(1, 1, layout="constrained", subplot_kw={"projection": "polar"})
ax.plot(phi1, Z_theor, "C0", label="Theoriekurve")
ax.plot(phi2, Z_theor, "C0")
ax.plot(arg, Z, "C1x", label="Messwerte")
ax.set_ylim(0, 600)
ax.set_xlabel(r"$\varphi \,/\, \mathrm{rad}$")
ax.text(0.67, 0.68, r"$|Z| \,/\, \mathrm{\Omega}$")
ax.set_thetagrids(
    [0, 45, 90, 135, 180, 225, 270, 315],
    labels=[
        r"$0$",
        r"$\frac{1}{4} \pi$",
        r"$\frac{1}{2} \pi$",
        r"$\frac{3}{4} \pi$",
        r"$\pm \pi$",
        r"$- \frac{3}{4} \pi$",
        r"$- \frac{1}{2} \pi$",
        r"$- \frac{1}{4} \pi$",
    ],
)
ax.grid(True)
ax.legend(bbox_to_anchor=(0.45, 0.8, 0, 0))
fig.savefig("loesung-polar.pdf")
# end solution
