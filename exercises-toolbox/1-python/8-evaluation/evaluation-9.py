metal_names = {"Fe": "Eisen",
               "Cu": "Kupfer"}


metal_densities = {"Fe": 7.87,
                    "Cu": 8.96}


metal_volumes = {"Fe": [10.0, 16.7, 23.5, 28.5, 34.9],
                 "Cu": [10.0, 19.7, 28.6, 39.4, 50.1]}


def calculate_metal_mass(volume, metal):
    density = metal_densities[metal]
    return density * volume

# Auch für Dictionaries gibt es eine Comprehension, die dict-comprehension:
metal_masses = {metal:

                [calculate_metal_mass(volume, metal=metal)
                for volume in volumes]

                for metal, volumes in metal_volumes.items()}


for metal, masses in metal_masses.items():
    print(f"Berechnete Massen für {metal_names[metal]}:")
    print(masses)
