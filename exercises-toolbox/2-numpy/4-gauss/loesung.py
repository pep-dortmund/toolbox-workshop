import numpy as np

rng = np.random.default_rng()
x_new = rng.normal(1.0, 2.0, 1000)

x_old = np.random.normal(1, 2, size=1000)

print("Summe, neu: ", np.sum(x_new))
print("Summe, alt:  ", np.sum(x_old))
