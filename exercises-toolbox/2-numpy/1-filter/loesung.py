import numpy as np

x, y = np.genfromtxt('data.txt', unpack=True)

selected = y[x > 0]

print('Mittelwert: ', np.mean(selected))
print('Standardabweichung: ', np.std(selected))
