density_iron = 7.87
density_copper = 8.96

volumes_iron = [10.0, 16.7, 23.5, 28.5, 34.9]
volumes_copper = [10.0, 19.7, 28.6, 39.4, 50.1]


print("Berechnete Massen für Eisen:")
for volume in volumes_iron:
    # Es ist grundsätzlich besser die Berechnung
    # und die Ausgabe von Ergebnissen von einander zu trennen
    # Zum Beispiel, um mit den berechneten Massen eine weitere Berechnung durchzuführen
    print(density_iron * volume)

print("Berechnete Massen für Kupfer:")
for volume in volumes_copper:
    # Es ist grundsätzlich besser die Berechnung
    # und die Ausgabe von Ergebnissen von einander zu trennen
    # Zum Beispiel, um mit den berechneten Massen eine weitere Berechnung durchzuführen
    print(density_copper * volume)
