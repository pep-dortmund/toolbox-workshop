import matplotlib.pyplot as plt
import numpy as np

# Datenfile erzeugen
data_x = np.linspace(0, 10, 50)
data_y = 10 * np.exp(-data_x)
np.savetxt("3.txt", np.column_stack([data_x, data_y]), header="x y")

x, y = np.genfromtxt("3.txt", unpack=True)

fig, (ax1, ax2) = plt.subplots(1, 2, constrained_layout=True)

ax1.plot(x, y, ".")
ax1.set_xlabel(r"$x$")
ax1.set_ylabel(r"$y$")

ax2.plot(x, y, ".")
ax2.set_xlabel(r"$x$")
ax2.set_ylabel(r"$y$")
ax2.set_yscale("log")

fig.savefig("loesung.pdf")
