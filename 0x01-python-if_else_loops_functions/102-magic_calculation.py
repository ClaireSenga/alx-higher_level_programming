#/usr/bin/python3

import dis

def magic_calculation(a, b, c):
    if a < b:
        return c
    elif c > b:
        return a + b
    else:
        return a * b - c

# Print the bytecode for the magic_calculation function
dis.dis(magic_calculation)

# Define sample values for a, b, and c
a = 5
b = 3
c = 7

# Call the function with the defined values
result = magic_calculation(a, b, c)
print("Result:", result)
