def histogram(nums):
    for num in nums:
        if num < 0:
            print('X')
        else:
            print(num * '*')


histogram([6, 2, -1, 10, 1, 8])
