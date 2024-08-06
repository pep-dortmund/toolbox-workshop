# begin solution
from scipy.constants import physical_constants

# Found using find() in IPython:
# from scipy.constants import find

for name in [
    "Planck constant",
    "electron mass",
    "weak mixing angle",
    "Boltzmann constant",
    "electron g factor",
]:
    print(name, physical_constants[name])
# end solution
