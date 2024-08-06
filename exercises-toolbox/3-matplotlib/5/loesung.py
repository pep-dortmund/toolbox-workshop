# begin solution
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi)

fig, ax = plt.subplots(1, 1, layout="constrained")

ax.plot(x, np.sin(x), label=r"$\sin(x)$")
ax.plot(x, np.cos(x), label=r"$\cos(x)$")

ax.set_xlim(0, 2 * np.pi)
ax.set_ylim(-1.2, 1.2)
ax.set_xlabel(r"$x$")

ax.set_xticks(
    np.arange(0, 2.1 * np.pi, np.pi / 2),
    [
        r"$0$",
        r"$\frac{1}{2}\pi$",
        r"$\pi$",
        r"$\frac{3}{2}\pi$",
        r"$2\pi$",
    ],
)

ax.legend()
fig.savefig("loesung.pdf")
# end solution
