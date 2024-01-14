#!/usr/bin/python3
'''module for Square class.'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''a square class.'''


    def __init__(self, size, x=0, y=0, id=None):
        '''constructor'''
        super().__init__(size, size, x, y, id)
        '''super class is called'''

    def __str__(self):
        '''Returns string info about this square.'''
        return '[{}] ({}) {}/{} - {}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        '''size of the square'''
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, id=None, size=None, x=None, y=None):
    '''method that updates instance attributes via */**args.'''
    if id is not None:
        self.id = id
    if size is not None:
        self.size = size
    if x is not None:
        self.x = x
    if y is not None:
        self.y = y

    def update(self, *args, **kwargs)
    '''updated example attributes via no-keyword & keyword args.'''
    #print(args, kwargs)
    if args:
        self.__update(*args)
    elif kwargs:
        self.__update(**kwargs)

    def to_dictionary(self, id, size, x, y):
        '''method that returns the dictionary display of the sqaure'''
         return{"id":self.id, "size":self.size, "x":self.x, "y":self.y}
