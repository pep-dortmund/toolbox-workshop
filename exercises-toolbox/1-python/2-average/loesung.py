data = [42, 3.1415, 2.7182, 1, 2]

# Hier den Mittelwert berechnen und ausgeben
# begin solution
avg = 0  # Define a variable and assign the value 0
for x in data:  # Loop over all entries in the list
    avg += x  # Add each value to the average variable
avg = avg / len(data)  # Divide by the number of entries in the list

print("Der Mittelwert ist ", avg)

# this is easier:
avg = sum(data) / len(data)
# The python function sum() calculates the sum of all elements

print("Der Mittelwert ist ", avg)
# end solution
