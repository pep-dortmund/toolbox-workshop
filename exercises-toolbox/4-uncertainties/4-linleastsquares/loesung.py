import matplotlib.pyplot as plt
import numpy as np
import os.path
import uncertainties as unc
import uncertainties.unumpy as unp

if not os.path.isfile("daten.txt"):
    print("creating data file")
    x = np.linspace(0, 2 * np.pi)
    y = 3 * np.sin(x) + 2 * np.cos(x) + np.random.normal(0, 0.1, len(x))
    np.savetxt("daten.txt", np.transpose([x, y]), header="x\ty")
    print("done")

def linleastsquares(functionlist, x_values, y_values):
    y = np.matrix(unp.nominal_values(y_values)).T
    Z = np.matrix(unc.covariance_matrix(y_values)).I

    # N rows vor every value, p columns for every function
    dim = (len(x_values), len(functionlist))

    A = np.matrix(np.zeros(dim))

    for i, func in enumerate(functionlist):
        A[:, i] = func(x_values)[:, np.newaxis]

    invATA = (A.T * Z * A).I
    params = invATA * A.T * Z * y

    cov = invATA

    return (np.array(unc.correlated_values(params.flat, np.array(cov))))

x, y = np.genfromtxt("daten.txt", unpack=True)
y = unp.uarray(y, 0.1)

params = linleastsquares([np.sin, np.cos], x, y)

for i, param in enumerate(params):
    print("Param", i, "=", unp.nominal_values(param), "±", unp.std_devs(param))

x_plot = np.linspace(0, 2 * np.pi, 100)

plt.errorbar(x, unp.nominal_values(y), yerr=unp.std_devs(y), fmt='k+', label="Daten")
plt.plot(x_plot, unp.nominal_values(params[0] * np.sin(x_plot) + params[1] * np.cos(x_plot)), 'b-', label="Fit")
plt.legend()
plt.savefig('loesung.pdf')
