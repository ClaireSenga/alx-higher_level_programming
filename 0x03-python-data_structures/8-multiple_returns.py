#!/usr/bin/python3
def multiple_returns(sentence):

    if len(sentence) == 0:
        return (None, None)  # 2 because it is a tuple

    else:
        return multiple_returns(len(sentence), sentence[0])
