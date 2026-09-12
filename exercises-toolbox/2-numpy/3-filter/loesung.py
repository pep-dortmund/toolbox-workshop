# begin solution
import numpy as np

# import the data, stored in two columns into the arrays x and y
x, y = np.genfromtxt("data.txt", unpack=True)

print(f"Es sind {np.sum(x > 0)} von {len(x)} Wertepaaren mit x > 0.")

# [x < 0] is a mask with the condition x < 0
# at every position where this is true,
# the corresponding y-value is then given to `selected`
selected = y[x < 0]

print("Mittelwert: ", np.mean(selected))
print("Standardabweichung: ", np.std(selected))
# end solution
