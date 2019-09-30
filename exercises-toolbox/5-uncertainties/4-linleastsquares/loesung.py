import matplotlib.pyplot as plt
import numpy as np
import uncertainties as unc
import uncertainties.unumpy as unp


def create_data():
    ''' Create the data file '''
    x = np.linspace(0, 2 * np.pi)
    y = 3 * np.sin(x) + 2 * np.cos(x) + np.random.normal(0, 0.2, len(x))
    np.savetxt("daten.txt", np.column_stack([x, y]), header="x y")


def linleastsquares(functions, x_values, y_values):
    y = unp.nominal_values(y_values)
    Z = np.linalg.inv(unc.covariance_matrix(y_values))

    A = np.column_stack([f(x_values) for f in functions])

    invATA = np.linalg.inv(A.T @ Z @ A)
    params = invATA @ A.T @ Z @ y

    cov = invATA

    return unc.correlated_values(params.flat, cov)


def linear_combination(x, functions, params):
    return np.sum([p * f(x) for p, f in zip(params, functions)], axis=0)


if __name__ == '__main__':
    create_data()

    x, y = np.genfromtxt("daten.txt", unpack=True)
    y = unp.uarray(y, 0.2)

    # remember, in python everything is an object,
    # so we can just create a list of functions.
    functions = [np.sin, np.cos]

    params = linleastsquares(functions, x, y)
    print(params)

    for i, param in enumerate(params):
        # for ufloat formatting see https://pythonhosted.org/uncertainties/user_guide.html
        print(f'p_{i} = {param:P}')

    x_plot = np.linspace(-0.1, 2 * np.pi + 0.1, 100)

    plt.errorbar(x, unp.nominal_values(y), yerr=unp.std_devs(y), fmt='k+', label="Daten")
    plt.plot(
        x_plot,
        unp.nominal_values(linear_combination(x_plot, functions, params)),
        label="Fit"
    )
    plt.xlabel(r'$x$')
    plt.ylabel(r'$y$')
    plt.xlim(-0.1, 2 * np.pi + 0.1)
    plt.legend()
    plt.savefig('loesung.pdf')
