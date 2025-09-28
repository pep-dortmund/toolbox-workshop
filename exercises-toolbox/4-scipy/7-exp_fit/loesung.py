from typing import Callable

import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt


def exponential(x: np.ndarray, a: float, b: float) -> np.ndarray:
    """Hier Funktion ergänzen"""
    # begin solution
    return a * np.exp(b * x)


x, y = np.genfromtxt("exp.txt", unpack=True)

mask = y > 0  # Nutze nur Werte größer 0 für die log-Trafo
y_fit = np.log(y[mask])
x_fit = x[mask]

params_poly, cov_poly = np.polyfit(x_fit, y_fit, deg=1, cov=True)
unc_poly = np.sqrt(np.diag(cov_poly))

# Wegen der Trafo sind a und b vertauscht und müssen deswegen wieder
# zurücktransformiert und getauscht werden
params_poly = np.array([np.exp(params_poly[1]), params_poly[0]])

print("np.polyfit:")
for name, value, uncertainty in zip("ab", params_poly, unc_poly):
    print(f"{name} = {value:.3f} ± {uncertainty:.3f}")

# end solution
# Hier polyfit Fit ergänzen
# params_poly, cov_poly = #
# unc_poly = #


# begin solution
params_curve, cov_curve = curve_fit(exponential, x, y)

unc_curve = np.sqrt(np.diag(cov_curve))

print("scipy.optimize.curve_fit:")
for name, value, uncertainty in zip("ab", params_curve, unc_curve):
    print(f"{name} = {value:.3f} ± {uncertainty:.3f}")

# end solution
# Hier curve_fit Fit ergänzen
# params_curve, cov_curve = #
# unc_curve = #


# Hier wird der Plot erstellt
def unc_band(
    x: np.ndarray,
    params: np.ndarray,
    unc: np.ndarray,
    **kwargs,
) -> None:
    """Visualize uncertainty."""
    ax.fill_between(
        x_lin,
        exponential(x_lin, *(params - unc)),
        exponential(x_lin, *(params + unc)),
        **kwargs,
    )


def plot_fit(
    x: np.ndarray,
    func: Callable | np.ndarray,
    params: np.ndarray,
    unc: np.ndarray = None,
    label="",
    **kwargs,
) -> None:
    """Plots the fit."""
    if isinstance(func, Callable):
        func = func(x, *params)

    text = (
        f"{label} ("
        + ", ".join(
            [
                f"{name} = {val:.2f} ± {un:.2f}"
                for name, val, un in zip("ab", params, unc)
            ]
        )
        + ")"
    )

    ax.plot(x, func, label=text, **kwargs)


x_lin = np.linspace(0, 5, 1000)

fig, axs = plt.subplot_mosaic(
    [["Linear", "Log"]], figsize=(10, 5), layout="constrained"
)

for ax in axs.values():
    ax.scatter(x, y, label="Daten", s=10, color="black")

    plot_fit(
        x_lin,
        exponential(x_lin, *params_poly),
        params_poly,
        unc_poly,
        label="polyfit",
        color="C1",
    )
    plot_fit(
        x_lin,
        exponential(x_lin, *params_curve),
        params_curve,
        unc_curve,
        label="curve_fit",
        color="C2",
    )

    unc_band(
        x_lin,
        params_poly,
        unc_poly,
        hatch=r"\\\\\\",
        facecolor="none",
        edgecolor="C1",
        alpha=0.4,
    )
    unc_band(
        x_lin,
        params_curve,
        unc_curve,
        color="C2",
        alpha=0.4,
    )

    ax.set(
        xlabel="x",
        ylabel="y",
        title=ax.get_label(),
    )
    ax.legend()

axs["Log"].set_yscale("log")
fig.savefig("loesung.pdf")
