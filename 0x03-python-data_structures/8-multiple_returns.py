#!/usr/bin/python3
def multiple_returns(sentence):
    my_tuple = ()
    if len(sentence) == 0:
        return (None, None)

    else:
        my_tuple = len(sentence), sentence[0]
    return my_tuple

sentence = "At school, I learnt C!"
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))
