metal_names = {"Fe": "Eisen",
               "Cu": "Kupfer"}


metal_densities = {"Fe": 7.87,
                    "Cu": 8.96}


metal_volumes = {"Fe": [10.0, 16.7, 23.5, 28.5, 34.9],
                 "Cu": [10.0, 19.7, 28.6, 39.4, 50.1]}


def calculate_metal_mass(volume, metal):
    density = metal_densities[metal]
    return density * volume

# Hier wird durch eine Schleife über ein Dictionary ein neues Dictionary erzeugt.
# Das geht (wie schon bei Listen) kompakter, wird  dadurch aber nicht unbedingt leserlicher!
metal_masses = {}

for metal, volumes in metal_volumes.items():
    metal_masses[metal] = [calculate_metal_mass(volume, metal=metal)
                           for volume in volumes]

for metal, masses in metal_masses.items():
    print(f"Berechnete Massen für {metal_names[metal]}:")
    print(masses)
