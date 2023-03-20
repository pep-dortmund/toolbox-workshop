import numpy as np
import matplotlib.pyplot as plt
from uncertainties import correlated_values
import uncertainties.unumpy as unp

time, length = np.genfromtxt("daten.txt", unpack=True)

popt, pcov = np.polyfit(time, length, deg=1, cov=True)
parameters = correlated_values(popt, pcov)

for name, para in zip('ab', parameters):
    print(f'{name} = {para}')

p = np.poly1d(unp.nominal_values(parameters))

fig, ax = plt.subplots()

ax.plot(time, length, ".", label="Messwerte")
ax.plot(time, p(time), "-", label="Fit")

ax.set_xlabel(r"$t \mathbin{/} \unit{\min}$")
ax.set_ylabel(r"$s \mathbin{/} \unit{\m}$")

ax.legend()
ax.grid()

fig.savefig("build/plot.pdf")

with open("build/parameters.tex", "w") as f:
    f.write(rf"a &= \qty{{{parameters[0]}}}{{\meter\per\second}} \\".replace("+/-", "+-"))
    f.write("\n")
    f.write(rf"b &= \qty{{{parameters[1]}}}{{\meter}}".replace("+/-", "+-"))
