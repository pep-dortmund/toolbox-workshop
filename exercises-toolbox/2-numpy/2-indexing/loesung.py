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

fig, ax = plt.subplots(1, 1, constrained_layout=True)
mat = ax.matshow(field, cmap="Set1", vmax=5, vmin=-1)
fig.savefig("Spielfeld_Beginn.pdf")
ax.cla()

# Lösung für Aufgabe 1:

# 2er Schiffe:
field[0, 6:8] = -1
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

# Lösung für Aufgaben 2:
field[:7:3, 2:6:3] = -1


print("Spielfeld zum Ende des Spiels:")
print(field)

mat = ax.matshow(field, cmap="Set1", vmax=5, vmin=-1)
fig.savefig("Spielfeld_Ende.pdf")
