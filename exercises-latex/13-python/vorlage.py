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
