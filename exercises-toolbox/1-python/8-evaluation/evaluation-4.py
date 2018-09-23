density_iron = 7.87
density_copper = 8.96

volumes_iron = [10.0, 16.7, 23.5, 28.5, 34.9]
volumes_copper = [10.0, 19.7, 28.6, 39.4, 50.1]

# Leere Liste zum speichern der Ergebnisse
masses_iron = []
for volume in volumes_iron:
    # Berechung der Massen und 'anhängen' an die Liste
    masses_iron.append(density_iron * volume)


# Leere Liste zum speichern der Ergebnisse
masses_copper = []
for volume in volumes_copper:
    # Berechung der Massen und 'anhängen' an die Liste
    masses_copper.append(density_copper * volume)


print("Berechnete Massen für Eisen:")
print(masses_iron)

print("Berechnete Massen für Kupfer:")
print(masses_copper)