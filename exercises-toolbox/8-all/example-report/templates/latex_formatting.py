import numpy as np
from uncertainties.unumpy import (
    std_devs as stds,
)

def make_qty(num, unit, exp="", figures=None, formatting=None):
    """Format an uncertainties ufloat as a \qty quantity"""
    if np.any(stds([num])):
        if figures is None:
            figures = ""
        x = f"{num:.{figures:}uf}".replace("/", "")
    else:
        x = f"{num:.{figures:}f}"
    if exp and not str(exp).startswith('e'):
        exp = 'e' + str(exp) 
    if formatting:
        return rf"\qty[{formatting}]{{{x}{exp}}}{{{unit}}}"

    return rf"\qty{{{x}{exp}}}{{{unit}}}"




