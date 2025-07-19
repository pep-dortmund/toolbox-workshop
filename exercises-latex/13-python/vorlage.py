import numpy as np
from uncertainties.unumpy import (
    std_devs as stds,
)


def make_qty(num, unit, exp="", figures=None):
    """Format an uncertainties ufloat as a \qty quantity"""
    if np.any(stds([num])):
        if figures is None:
            figures = ""
        x = "{0:.{1:}uf}".format(num, figures).replace("/", "")
    else:
        x = "{0:.{1:}f}".format(num, figures)

    return rf"\qty{{{x}{exp}}}{{{unit}}}"
