#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    # prints matrix of integers

    for row in matrix:
        for num in row:
            print("{:3}".format(num), end=' ')  # first 3
        print()  # move to next line
