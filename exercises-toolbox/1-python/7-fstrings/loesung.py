# Für die 1. und 2. Aufgabe:
title = "Wiegen von Metallen"
date = "24.09.2018"

# Für die 3. Aufgabe:
metals = ["Eisen", "Kupfer", "Zink", "Blei"]
masses = [9.1, 10.29, 12.485, 130.01]

# Für die 1. Aufgabe:
# Gewünschte Ausgabe:
# Versuch: Wiegen von Metallen durchgeführt am 24.09.2018
print()
# begin solution
print("Versuch:", title, "durchgeführt am", date)
# end solution

# Ausgabe mit Anführungszeichen:
# Versuch 'Wiegen von Metallen' durchgeführt am 24.09.2018
print()
# begin solution
print("Versuch:", "'" + title + "'", "durchgeführt am", date)
# end solution

# Für die 2. Aufgabe:
# print(f"")
# begin solution
print()  # Für den Abstand zur letzten Lösung
# Versuch: Wiegen von Metallen durchgeführt am 24.09.2018
print(f"Versuch: {title} durchgeführt am {date}")

# Versuch 'Wiegen von Metallen' durchgeführt am 24.09.2018
print(f"Versuch: '{title}' durchgeführt am {date}")
# end solution

# Für die 3.Aufgabe:
# begin solution
print()  # Für den Abstand zur letzten Lösung
# end solution
for metal, mass in zip(metals, masses, strict=False):
    print()
    # begin solution
    print(f"{metal}: {mass}")
    # end solution

# Gewünschte Ausgabe:
# Eisen: 9.1
# Kupfer: 10.29
# Zink: 12.485
# Blei: 130.01

# begin solution
# Für die 4.Aufgabe:
print()  # Für den Abstand zur letzten Lösung
for metal, mass in zip(metals, masses, strict=False):
    print(f"{metal}: {mass:0.2f}")


# Zum Knobeln für Interessierte:
# Wie funktioniert das hier?
print()  # Für den Abstand zur letzten Lösung
for metal, mass in zip(metals, masses, strict=False):
    offset = 11 - len(metal)
    print(f"{metal}:", f"{mass:>{offset}.2f}")
# end solution
