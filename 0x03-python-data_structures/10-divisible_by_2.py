#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    # finds all multiples of 2 in list

    res = []  # initialise to store new results

    for num in my_list:
        if num % 2 == 0:
            return res.append(True)

        else:
            res.append(False)
            
    return res