title = "Wiegen von Metallen"
date = "24.09.2018"

# Für die 3. Aufgabe:
metals = ["Eisen", "Kupfer", "Zink", "Blei"]
masses = [9.1, 10.29, 12.485, 130.01]

# Für die 1. Aufgabe:
# Versuch: Wiegen von Metallen durchgeführt am 24.09.2018
print("Versuch:", title, "durchgeführt am", date)

# Versuch 'Wiegen von Metallen' durchgeführt am 24.09.2018
print("Versuch:", "'" + title + "'", "durchgeführt am", date)

# Für die 2. Aufgabe:
print()  # Für den Abstand zur letzten Lösung
# Versuch: Wiegen von Metallen durchgeführt am 24.09.2018
print(f"Versuch: {title} durchgeführt am {date}")

# Versuch 'Wiegen von Metallen' durchgeführt am 24.09.2018
print(f"Versuch: '{title}' durchgeführt am {date}")

# Für die 3.Aufgabe:
print()  # Für den Abstand zur letzten Lösung
for metal, mass in zip(metals, masses):
    print(f"{metal}: {mass}")


# Für die 4.Aufgabe:
print()  # Für den Abstand zur letzten Lösung
for metal, mass in zip(metals, masses):
    print(f"{metal}: {mass:0.2f}")


# Zum Knobeln für Interessierte:
# Wie funktioniert das hier?
print()  # Für den Abstand zur letzten Lösung
for metal, mass in zip(metals, masses):
    offset = 11 - len(metal)
    print(f"{metal}:", f"{mass:>{offset}.2f}")
