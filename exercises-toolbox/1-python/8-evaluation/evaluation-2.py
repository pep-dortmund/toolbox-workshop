density_iron = 7.87
density_copper = 8.96

# Speichern aller Messwerte in Listen, je eine Liste pro Metall
volumes_iron = [10.0, 16.7, 23.5, 28.5, 34.9]
volumes_copper = [10.0, 19.7, 28.6, 39.4, 50.1]


print("Berechnete Massen für Eisen:")
# Zugriff durch '[]' auf die Messwerte in der Messwertliste
print(density_iron * volumes_iron[0])
print(density_iron * volumes_iron[1])
print(density_iron * volumes_iron[2])
print(density_iron * volumes_iron[3])
print(density_iron * volumes_iron[4])

print("Berechnete Massen für Kupfer:")
# Zugriff durch '[]' auf die Messwerte in der Messwertliste
print(density_copper * volumes_copper[0])
print(density_copper * volumes_copper[1])
print(density_copper * volumes_copper[2])
print(density_copper * volumes_copper[3])
print(density_copper * volumes_copper[4])


