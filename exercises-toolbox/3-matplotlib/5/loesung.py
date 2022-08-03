import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi)

plt.figure(constrained_layout=True)

plt.plot(x, np.sin(x), label=r"$\sin(x)$")
plt.plot(x, np.cos(x), label=r"$\cos(x)$")

plt.xlim(0, 2 * np.pi)
plt.ylim(-1.2, 1.2)
plt.xlabel(r"$x$")

plt.xticks(
    np.arange(0, 2.1 * np.pi, np.pi / 2),
    [
        r"$0$",
        r"$\frac{1}{2}\pi$",
        r"$\pi$",
        r"$\frac{3}{2}\pi$",
        r"$2\pi$",
    ],
)

plt.legend()
plt.savefig("loesung.pdf")
