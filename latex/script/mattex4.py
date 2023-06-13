import matplotlib as mpl
mpl.use("pgf")
import matplotlib.pyplot as plt
import numpy as np
mpl.rcParams.update(
    {
        "font.family": "serif",
        "text.usetex": True,
        "pgf.rcfonts": False,
        "pgf.texsystem": "lualatex",
        "pgf.preamble": r"\input{header-matplotlib.tex}",  # <-- move header to file
    }
)

x = np.linspace(0, 10, 1000)
y = x ** np.sin(x)
# set figure size and use constrained_layout
fig = plt.figure(figsize=(6.022, 3.39), layout="constrained")
ax = fig.add_subplot(111)
ax.plot(x, y)
ax.set_xlabel(r"$\alpha \mathbin{/} \unit{\ohm}$")

fig.savefig("build/figures/mattex4.pdf", bbox_inches="tight", pad_inches=0)
