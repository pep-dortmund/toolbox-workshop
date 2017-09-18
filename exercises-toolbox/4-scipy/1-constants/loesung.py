from scipy.constants import find, physical_constants

# Found using find() in IPython:

for name in [
        'Planck constant',
        'electron mass',
        'weak mixing angle',
        'Boltzmann constant',
        'electron g factor',
        ]:
    print(name, physical_constants[name])
