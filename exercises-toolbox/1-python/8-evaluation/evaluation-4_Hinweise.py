density_iron = 7.87
density_copper = 8.96

volumes_iron = [10.0, 16.7, 23.5, 28.5, 34.9]
volumes_copper = [10.0, 19.7, 28.6, 39.4, 50.1]


masses_iron = []
for volume in volumes_iron:
    # In der Berechnung, die Berechnung  die hier ausgeführt wird ändert
    # sich nur das Volumen und diese wird unten für Kupfer noch einmal wiederholt
    masses_iron.append(density_iron * volume)

masses_copper = []
for volume in volumes_copper:
    masses_copper.append(density_copper * volume)


print("Berechnete Massen für Eisen:")
print(masses_iron)

print("Berechnete Massen für Kupfer:")
print(masses_copper)