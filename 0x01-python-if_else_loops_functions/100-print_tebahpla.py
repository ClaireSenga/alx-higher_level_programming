#!/usr/bin/python3

for i in range(122, 96, -1):
    print("{}".format(chr(i).lower() if (122 - i) % 2 == 0 else chr(i).upper(), end=''))
