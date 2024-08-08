#! /usr/bin/env python
# encoding: utf-8

import numpy as np
import matplotlib.pyplot as plt

field = np.array(
    [
        [4, 0, 1, 0, 0, 1, 2, 2, 0, 0],
        [4, 0, 2, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 2, 0, 0, 0, 0, 3, 3, 3],
        [4, 0, 1, 0, 0, 1, 0, 0, 0, 0],
        [0, 3, 0, 2, 2, 0, 3, 0, 4, 0],
        [0, 3, 0, 0, 0, 0, 3, 0, 4, 0],
        [0, 3, 1, 0, 0, 1, 3, 0, 4, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 4, 0],
        [2, 0, 0, 5, 5, 5, 5, 5, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
)

print("Spielfeld zu Beginn des Spiels:")
print(field)

# begin solution
# comment for vorlage.py
# end solution
# Was das hier ist lernen wir noch, kann getrost ignoriert werden.
# In der Zwischenzeit die Kurzfassung: Das 'macht' die Bilder.
fig, ax = plt.subplots(1, 1, layout="constrained")
mat = ax.matshow(field, cmap="Set1", vmax=5, vmin=-1)
fig.savefig("Spielfeld_Loesung_Beginn.pdf")

# Hier die Lösung für Aufgabe 1 und 2 eintragen (ein Beispiel ist angegeben):
# Durch Ausführen dieser Datei kann Schritt für Schritt der Fortschritt
# überprüft werden.
field[0, 6:8] = -1
# begin solution
# Lösung für Aufgabe 1:

# 2er Schiffe:
# field[0, 6:8] = -1
field[1:3, 2] = -1
field[4, 3:5] = -1
field[7:9, 0] = -1

# 3er Schiffe:
field[2, 7:10] = -1
field[4:7, 1] = -1
field[4:7, 6] = -1
# Die letzten beiden gehen auch auf einmal:
# field[4:7, 1:7:5] = -1

# 4er Schiffe:
field[:4, 0] = -1
field[4:8, 8] = -1

# 5er Schiff:
field[8, 3:8] = -1

# Lösung für Aufgabe 2:
field[:7:3, 2:6:3] = -1

# Mit Masken geht alles noch einfacher!

# end solution

print("Spielfeld zum Ende des Spiels:")
print(field)

# begin solution
# comment for vorlage.py
# end solution
# Was das hier ist lernen wir noch, kann getrost ignoriert werden.
# In der Zwischenzeit die Kurzfassung: Das 'macht' die Bilder.
mat.set_array(field)
fig.savefig("Spielfeld_Loesung_Ende.pdf")
