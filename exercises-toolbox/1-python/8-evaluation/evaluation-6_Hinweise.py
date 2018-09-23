density_iron = 7.87
density_copper = 8.96

volumes_iron = [10.0, 16.7, 23.5, 28.5, 34.9]
volumes_copper = [10.0, 19.7, 28.6, 39.4, 50.1]

def calculate_metal_mass(volume, metal):
    if metal == "Fe":
        density = density_iron
    elif metal == "Cu":
        density = density_copper

    return density * volume


# Diese Schleife zur Berechnung von Werten die in eine neue Liste
# geschrieben werden kann man etwas kompakter schreiben.
# Das Ergebnis ist äquivalent!
masses_iron = []
for volume in volumes_iron:
    masses_iron.append(calculate_metal_mass(volume, metal="Fe"))

# Diese Schleife zur Berechnung von Werten die in eine neue Liste
# geschrieben werden kann man etwas kompakter schreiben.
# Das Ergebnis ist äquivalent!
masses_copper = []
for volume in volumes_copper:
    masses_copper.append(calculate_metal_mass(volume, metal="Cu"))


print("Berechnete Massen für Eisen:")
print(masses_iron)

print("Berechnete Massen für Kupfer:")
print(masses_copper)