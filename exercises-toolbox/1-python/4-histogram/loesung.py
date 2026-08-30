# begin solution
def histogram(nums):  # define the function and place the incoming data
    for num in nums:  # iterate over the elements in the list
        if num < 0:  # Check for negative numbers
            print("X")
        else:
            print(num * "*")  # print the appropriate number of stars


# end solution
histogram([6, 2, -1, 10, 1, 8])
