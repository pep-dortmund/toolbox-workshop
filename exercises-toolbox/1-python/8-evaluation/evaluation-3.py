density_iron = 7.87
density_copper = 8.96

volumes_iron = [10.0, 16.7, 23.5, 28.5, 34.9]
volumes_copper = [10.0, 19.7, 28.6, 39.4, 50.1]


print("Berechnete Massen für Eisen:")
# Verwendung einer for-Schleife, um die Berechnung für alle Messwerte in der Liste auszuführen
for volume in volumes_iron:
    print(density_iron * volume)

print("Berechnete Massen für Kupfer:")
# Verwendung einer for-Schleife, um die Berechnung für alle Messwerte in der Liste auszuführen
for volume in volumes_copper:
    print(density_copper * volume)
