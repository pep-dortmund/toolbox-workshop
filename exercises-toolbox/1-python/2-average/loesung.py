data = [42, 3.1415, 2.7182, 1, 2]

# Hier den Mittelwert berechnen und ausgeben
# begin solution
avg = 0
for x in data:
    avg += x
avg = avg / len(data)

print("Der Mittelwert ist ", avg)

# this is easier:
avg = sum(data) / len(data)

print("Der Mittelwert ist ", avg)
# end solution
