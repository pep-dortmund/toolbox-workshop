import numpy as np

x, y = np.genfromtxt("data.txt", unpack=True)

print(f"Es sind {np.sum(x > 0)} von {len(x)} Wertepaaren mit x > 0.")

selected = y[x < 0]

print("Mittelwert: ", np.mean(selected))
print("Standardabweichung: ", np.std(selected))
