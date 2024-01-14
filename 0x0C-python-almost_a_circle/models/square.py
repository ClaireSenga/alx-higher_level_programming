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
