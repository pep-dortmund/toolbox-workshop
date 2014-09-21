
from numpy import genfromtxt, mean, std

x, y = genfromtxt('data.txt', unpack=True)

selected = y[x > 0]

print('Mittelwert: ', mean(selected))
print('Standardabweichung: ', std(selected))


