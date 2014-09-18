# encoding: utf-8
from __future__ import (print_function,
                        division,
                        unicode_literals,
                        absolute_import)

import numpy as np
import scipy.optimize
import uncertainties as unc
import uncertainties.unumpy as unp

def ucurve_fit(f, x, y, **kwargs):
    if np.any(unp.std_devs(y) == 0):
        sigma = None
    else:
        sigma = unp.std_devs(y)

    popt, pcov = scipy.optimize.curve_fit(f, x, unp.nominal_values(y), sigma=sigma, **kwargs)

    return unp.uarray(popt, np.sqrt(np.diag(pcov)))
