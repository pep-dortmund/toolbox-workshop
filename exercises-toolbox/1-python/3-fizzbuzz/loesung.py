for n in range(1, 101):
    # Programm ergänzen / ändern
    # begin solution
    if n % 3 == 0 and n % 5 == 0:
        print("Fizzbuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        # end solution
        print(n)
