#!/usr/bin/python3

if __name__ == "__main__":
    # Prints all names defined by hidden_4 module

    import hidden_4

    names = dir(hidden_4)  # lists all names

    for name in names:  #repeats through names
        if name[:2] != "__":
            print(name)
