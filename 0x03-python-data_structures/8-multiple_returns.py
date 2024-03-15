#!/usr/bin/python3
def multiple_returns(sentence):
    # a tuple with len of string & 1st char

    if len(sentence) == 0:
        return (None, None)  # 2 because it is a tuple

    else:
        return multiple_returns(len(sentence), sentence[0])
