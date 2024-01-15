#!/usr/bin/python3
'''module for base class'''

class Base:
    '''a representation f the base of our OOP hierachy'''

    __nb_objects = 0
    '''private class attribute'''

    def __init__(self, id=None):
        '''Constructor'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''static method that returns the JSON representation of list_dictionaries.'''
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
