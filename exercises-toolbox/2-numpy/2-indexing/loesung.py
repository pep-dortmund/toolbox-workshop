#! /usr/bin/env python
# encoding: utf-8

import numpy as np
import matplotlib.pyplot as plt

field = np.array([[4, 0, 1, 0, 0, 1, 2, 2, 0, 0],
                  [4, 0, 2, 0, 0, 0, 0, 0, 0, 0],
                  [4, 0, 2, 0, 0, 0, 0, 3, 3, 3],
                  [4, 0, 1, 0, 0, 1, 0, 0, 0, 0],
                  [0, 3, 0, 2, 2, 0, 3, 0, 4, 0],
                  [0, 3, 0, 0, 0, 0, 3, 0, 4, 0],
                  [0, 3, 1, 0, 0, 1, 3, 0, 4, 0],
                  [2, 0, 0, 0, 0, 0, 0, 0, 4, 0],
                  [2, 0, 0, 5, 5, 5, 5, 5, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

print("Spielfeld zu Beginn des Spiels:")
print(field)

mat = plt.matshow(field, cmap="Set1", vmax=5, vmin=-1)
plt.savefig("Spielfeld_Beginn.pdf")

# Hier die Lösung für Aufgabe 1 eintragen (ein Beisiel ist angegeben):
field[0, 6:8] = -1


print("Spielfeld zum Ende des Spiels:")
print(field)

mat = plt.matshow(field, cmap="Set1", vmax=5, vmin=-1)
plt.savefig("Spielfeld_Ende.pdf")