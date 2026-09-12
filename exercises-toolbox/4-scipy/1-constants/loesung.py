# begin solution
from scipy.constants import find, physical_constants

print("Planck", find("Planck"))
print("electron", find("electron"))
print("angle", find("angle"))
print("Boltzmann", find("Boltzmann"))
print("g factor", find("g factor"))

print("\nAusgabe der Werte:")

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
