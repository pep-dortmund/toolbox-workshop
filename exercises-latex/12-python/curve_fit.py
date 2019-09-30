import numpy as np
import scipy.optimize
import uncertainties as unc
import uncertainties.unumpy as unp


def ucurve_fit(f, x, y, **kwargs):
    '''
    Uncertainties wrapper around curve_fit
    y can be a uarray with uncertainties
    and the parameters are returned as uncertainties.correlated_values
    '''
    if np.any(unp.std_devs(y) == 0):
        sigma = None
    else:
        sigma = unp.std_devs(y)

    popt, pcov = scipy.optimize.curve_fit(
        f,
        x,
        unp.nominal_values(y),
        sigma=sigma,
        absolute_sigma=True,
        **kwargs,
    )

    return unc.correlated_values(popt, pcov)
