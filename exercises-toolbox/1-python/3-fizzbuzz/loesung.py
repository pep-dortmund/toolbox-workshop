for n in range(1, 101):
    # Programm ergänzen / ändern
    # begin solution
    # The order is important, try it out.
    if n % 3 == 0 and n % 5 == 0:  # check for divisibility by 3 and 5
        print("Fizzbuzz")
    elif n % 3 == 0:  # check for divisibility by 3
        print("Fizz")
    elif n % 5 == 0:  # check for divisibility by 5
        print("Buzz")
    else:
        # end solution
        print(n)
