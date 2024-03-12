#!/usr/bin/python3
for char in range(97, 123): #97 to 123 is lowercase
    if chr(char) not in ['e' , 'q']:
        print("{}".format(chr(char)), end='')
