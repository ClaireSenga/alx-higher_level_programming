#!/usr/bin/python3

def fizzbuzz():
    for fixxbuzz in range(1, 101):
        if fizzbuzz % 3 == 0:
            print("Fizz",end=' ')

        elif fizzbuzz % 5 == 0:
            print("Buzz",end=' ')

        elif fizzbuzz % 5 == 0 and fizzbuzz % 3 == 0:
            print("FizzBuzz",end=' ')

        else:
            print(fizzbuzz,end=' ') #remaining numbers


