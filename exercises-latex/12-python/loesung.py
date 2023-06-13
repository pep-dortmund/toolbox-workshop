import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from uncertainties.unumpy import (
    nominal_values as noms,
    std_devs as stds,
)

from curve_fit import ucurve_fit


def make_qty(num, unit, exp="", figures=None):
    """Format an uncertainties ufloat as a \qty quantity"""
    if np.any(stds([num])):
        if figures is None:
            figures = ""
        x = "{0:.{1:}uf}".format(num, figures).replace("/", "")
    else:
        x = "{0:.{1:}f}".format(num, figures)

    return r"\qty{{{}{}}}{{{}}}".format(x, exp, unit)


t, U, U_err = np.genfromtxt("data.txt", unpack=True)
t *= 1e-3
U = 1e3 * unp.uarray(U, U_err)


def f(t, a, b, c, d):
    return a * np.sin(b * t + c) + d


params = ucurve_fit(f, t, U, p0=[1e3, 1e3, 0, 0])

t_plot = np.linspace(-0.5, 2 * np.pi + 0.5, 1000) * 1e-3

fig, ax = plt.subplots(1, 1, layout="constrained")

ax.errorbar(
    t * 1e3,
    noms(U) * 1e-3,
    yerr=stds(U) * 1e-3,
    fmt="k_",
    label="Daten",
)
ax.plot(t_plot * 1e3, f(t_plot, *noms(params)) * 1e-3, '-', label='Fit')
ax.set_xlim(t_plot[0] * 1e3, t_plot[-1] * 1e3)
ax.set_xlabel(r"$t \mathbin{/} \unit{\milli\second}$")
ax.set_ylabel(r"$U \mathbin{/} \unit{\kilo\volt}$")
ax.legend(loc="best")
fig.savefig("build/loesung-plot.pdf")

t1, t2 = np.array_split(t * 1e3, 2)
U1, U2 = np.array_split(U * 1e-3, 2)


table_header = r"""
  \begin{tabular}{
    S[table-format=1.3]
    S[table-format=-1.2]
    @{${}\pm{}$}
    S[table-format=1.2]
    @{\hspace*{3em}\hspace*{\tabcolsep}}
    S[table-format=1.3]
    S[table-format=-1.2]
    @{${}\pm{}$}
    S[table-format=1.2]
  }
    \toprule
    {$t \mathbin{/} \unit{\milli\second}$} & \multicolumn{2}{c}{$U \:/\: \unit{\kilo\volt}$\hspace*{3em}} &
    {$t \mathbin{/} \unit{\milli\second}$} & \multicolumn{2}{c}{$U \:/\: \unit{\kilo\volt}$} \\
    \midrule
"""

table_footer = r"""    \bottomrule
  \end{tabular}
"""
row_template = (
    r"    {0:1.3f} & {1.n:1.2f} & {1.s:1.2f} & {2:1.3f} & {3.n:1.2f} & {3.s:1.2f} \\"
)


with open("build/loesung-table.tex", "w") as f:
    f.write(table_header)
    for row in zip(t1, U1, t2, U2):
        f.write(row_template.format(*row))
        f.write("\n")
    f.write(table_footer)


a, b, c, d = params

with open("build/loesung-a.tex", "w") as f:
    f.write(make_qty(a * 1e-3, r"\kilo\volt"))

with open("build/loesung-b.tex", "w") as f:
    f.write(make_qty(b * 1e-3, r"\kilo\hertz"))

with open("build/loesung-c.tex", "w") as f:
    f.write(make_qty(c, ""))

with open("build/loesung-d.tex", "w") as f:
    f.write(make_qty(d * 1e-3, r"\kilo\volt"))
