import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

PROPERTIES = {
    "font.size": 18.0,
    "lines.linewidth": 2.5,
    "axes.labelsize": "medium",
    "axes.labelcolor": "222222",
    "axes.axisbelow": True,
    "xtick.labelsize": "medium",
    "ytick.labelsize": "medium",
    "xtick.color": "222222",
    "xtick.direction": "out",
    "ytick.color": "222222",
    "ytick.direction": "out",
}

plt.rcParams.update(PROPERTIES)


x, y = np.genfromtxt("./script/example_plot_data.txt", unpack=True)


def fit(x: np.ndarray, i0: float, mu: float, sigma: float) -> np.ndarray:
    """Gaussian Fit function.

    Parameters
    ----------
    x : array_like
        x data.
    i0 : float
        Amplitude.
    mu : float
        Mean.
    sigma : float
        Standard deviation
    """
    return i0 * np.exp(-2 * (x - mu) ** 2 / sigma**2)


params, _ = curve_fit(fit, x, y)
x_lin = np.linspace(0, 14, 1000)


fig, ax = plt.subplots(figsize=(7, 5), layout="constrained")

ax.plot(x, y, "x", ms=8, mew=2, color="#4d4742", label="Data")
ax.plot(x_lin, fit(x_lin, *params), color="#83B818", label="Fit")

ax.set(
    xlabel=r"$x \mathbin{/} \unit{\milli\metre}$",
    ylabel=r"$I \mathbin{/} \unit{\micro\ampere}$",
)
ax.legend()

fig.savefig("./build/example_plot.pdf")
