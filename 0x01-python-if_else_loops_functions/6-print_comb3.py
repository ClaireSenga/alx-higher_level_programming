#!/usr/bin/python3
for i in range(10):
    for j in range(i + 1, 10):   # to avoid repetition
        print("{:d}{:d},".format(i, j), end=' ' if i != 8 or j != 9 else '')

# Print the combination 89 separately
print("89")
