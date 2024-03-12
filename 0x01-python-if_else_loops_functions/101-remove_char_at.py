#!/usr/bin/python3

def remove_char_at(s, n):
    # Check if n is valid index
    if n < 0 or n >= len(s):
        return s  # Return the original string if n is out of range

    # Return string with char at index n removed
    return s[:n] + s[n+1:]
