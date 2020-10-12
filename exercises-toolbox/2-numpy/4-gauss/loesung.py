import numpy as np

x_new = np.random.default_rng().normal(1., 2., 1000)
x_old = np.random.normal(1, 2, size=1000)
print('Summe, neu: ', np.sum(x_new))
print('Summe, alt:  ', np.sum(x_old))
