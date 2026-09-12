# begin solution
import numpy as np

# This is the new, better way
# create a RandomNumberGenerator, as an argument you could give a seed
rng = np.random.default_rng()
# draw 1000 samples from a normal(gauss) distribution
# one rng can be used to draw samples from different distributions
x_new = rng.normal(1.0, 2.0, 1000)

# The old way, don't use this, but you might see it
x_old = np.random.normal(1, 2, size=1000)

print("Summe, neu: ", np.sum(x_new))
print("Summe, alt: ", np.sum(x_old))
# end solution
