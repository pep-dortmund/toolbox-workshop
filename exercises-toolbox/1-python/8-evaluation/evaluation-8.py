# Verpacken der Information über die Metalle in Dictionaries

# Die Schlüssel (keys) sind die Abkürzungen der Elemente im PSE
# die Werte (values) sind die Namen der Metalle
metal_names = {"Fe": "Eisen",
               "Cu": "Kupfer"}

# Die Schlüssel (keys) sind die Abkürzungen der Elemente im PSE
# die Werte (values) sind die Dichten der Metalle
metal_densities = {"Fe": 7.87,
                    "Cu": 8.96}

# Die Schlüssel (keys) sind die Abkürzungen der Elemente im PSE
# die Werte (values) sind die Messwerte der Volumen der Metalle
metal_volumes = {"Fe": [10.0, 16.7, 23.5, 28.5, 34.9],
                 "Cu": [10.0, 19.7, 28.6, 39.4, 50.1]}


def calculate_metal_mass(volume, metal):
    # Ersetzen der if-Bedingung durch 'nachschlagen' im Dichten-Dict
    density = metal_densities[metal]
    return density * volume




# Erstellen eines neuen Dicts für die Ergebnisse für die Massen:
# Die Schlüssel (keys) werden die Abkürzungen der Elemente im PSE sein
# die Werte (values) sind die Massen der Metalle
metal_masses = {}

# Simultane Schleife über die keys und values des Messwerte-Dicts
for metal, volumes in metal_volumes.items():
    # Zuweisung der berechneten Massen als Wert (value)
    # unter dem jeweiligen Metall als Schlüssel (key)
    # im neuen Massen-Dict
    metal_masses[metal] = [calculate_metal_mass(volume, metal=metal)
                           for volume in volumes]

# Ausgabe der Ergebnisse durch eine simultane Schleife über
# die keys (Metalle) und values (Massen) im Massen-Dict
for metal, masses in metal_masses.items():
    # Für die Ausgabe des deutschen Namens des Metalls wird dieser im
    # Namen-Dict 'nachgeschlagen' und mithilfe eines f-Strings ausgegeben
    print(f"Berechnete Massen für {metal_names[metal]}:")
    # Hier werden die jeweiligen Ergebnisse (Massen) ausgeben
    print(masses)
