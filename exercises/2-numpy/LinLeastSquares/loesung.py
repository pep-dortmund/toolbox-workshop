import matplotlib.pyplot as plt
import numpy as np
import os.path

if not os.path.isfile("daten.txt"):
    print("creating data file")
    x = np.linspace(0, 2*np.pi)
    y = 3*np.sin(x) + 2*np.cos(x) + np.random.normal(0, 0.1, len(x))
    np.savetxt("daten.txt", np.transpose([x, y]), header="x\ty")
    print("done")

def linleastsquares(functionlist, x_values, y_values, sigma):

    y_values = np.matrix(y_values).T

    # N rows vor every value, p columns for every function
    dim = (len(x_values), len(functionlist))

    A = np.matrix(np.zeros(dim))

    for i, x in enumerate(x_values):
        for j, func in enumerate(functionlist):
            A[i,j] = func(x)


    invATA = (A.T * A).I
    params = invATA * A.T * y_values

    cov = sigma**2 * invATA

    return np.array(params.flat), cov

x, y = np.genfromtxt("daten.txt", unpack=True)

params, cov = linleastsquares([np.sin, np.cos], x, y, 0.1)

for i, param in enumerate(params):
    print("Param", i, "=", param, "+-", np.sqrt(cov[i,i]))

x_plot = np.linspace(0, 2*np.pi, 100)

plt.errorbar(x, y, yerr=0.1, fmt='k+', label="Daten")
plt.plot(x_plot, params[0]*np.sin(x_plot) + params[1]*np.cos(x_plot), 'b-', label="Fit")
plt.legend()
plt.show()
