density_iron = 7.87
density_copper = 8.96

volumes_iron = [10.0, 16.7, 23.5, 28.5, 34.9]
volumes_copper = [10.0, 19.7, 28.6, 39.4, 50.1]



# Diese beiden Funktionen sind im Grunde die selbe, unterscheiden sich nur
# durch das jeweilige Metall.
def calculate_iron_mass(volume):
    return density_iron * volume

def calculate_copper_mass(volume):
    return density_copper * volume


masses_iron = []
for volume in volumes_iron:
    masses_iron.append(calculate_iron_mass(volume))


masses_copper = []
for volume in volumes_copper:
    masses_copper.append(calculate_copper_mass(volume))


print("Berechnete Massen für Eisen:")
print(masses_iron)

print("Berechnete Massen für Kupfer:")
print(masses_copper)