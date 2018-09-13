import IPython

def shoesize_and_age(shoesize, birth_year):
    step_1 = shoesize * 5
    step_2 = step_1 + 50
    step_3 = step_2 * 20
    step_4 = step_3 + 1017
    step_5 = step_4 - birth_year

    #IPython.embed()

    return step_5


print(shoesize_and_age(45, 1993))
