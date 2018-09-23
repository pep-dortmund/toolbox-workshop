density_iron = 7.87
density_copper = 8.96

volumes_iron = [10.0, 16.7, 23.5, 28.5, 34.9]
volumes_copper = [10.0, 19.7, 28.6, 39.4, 50.1]

# Verallgemeinerung der beiden Funktionen zur Berechnung der Masse,
# das Metall kann nun durch den zweiten Funktionsparameter angegeben.
def calculate_metal_mass(volume, metal):
    # if-Abfrage, um die Dichte für das jeweilige Metall auszuwählen
    if metal == "Fe":
        density = density_iron
    elif metal == "Cu":
        density = density_copper

    return density * volume


masses_iron = []
for volume in volumes_iron:
    # Aufruf der neuen Funktion zur Berechnung des Ergebnisses mit
    # dem zweiten Argument 'Fe' für Eisen
    masses_iron.append(calculate_metal_mass(volume, "Fe"))


masses_copper = []
for volume in volumes_copper:
    # Aufruf der neuen Funktion zur Berechnung des Ergebnisses mit
    # dem zweiten Argument 'Cu' für Eisen.
    # Es ist zu empfehlen die namen der parameter mit anzugeben,
    # damit man beim Lesen ihre Bedeutung versteht.
    masses_copper.append(calculate_metal_mass(volume, metal="Cu"))


print("Berechnete Massen für Eisen:")
print(masses_iron)

print("Berechnete Massen für Kupfer:")
print(masses_copper)