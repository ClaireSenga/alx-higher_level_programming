#!/usr/bin/python3
'''module for base class Rectangle'''
from model.base import Base

class Rectangle(Base):
    '''inherited class Rectangle'''

    def __init__(self, width, height, x=0, y=0, id=None):
       '''constructor'''
       super().__init__(id) 
       '''super class is called'''
       self.width = width
       self.height = height
       self.x = x
       self.y = y 

    @property
    def width(self):
        '''width of the rectangle'''
        return self.__width
    
    @width.setter
    def width(self, value):
        self.validate_integer("width", value, False)
        self.__width = value

    @property
    def height(self):
        '''height of the rectangle'''
        return self.__height
    
    @height.setter
    def height(self, value):
        self.validate_integer("height", value, False)
        self.__height = value

    @property
    def x(self):
        '''x of the rectangle'''
        return self.__x
    
    @x.setter
    def x(self, value):
        self.validate_integer("x", value)
        self.__x = value

    @property
    def y(self):
        '''y of the rectangle'''
        return self.__y
    
    @y.setter
    def y(self, value):
        self.validate_integer("y", value)
        self.__y = value

    def validate_integer(self, name, value, eq=True):
        '''method for validating the value'''
        if type(value) =! int:
            raise TypeError("{} must be an integer".format(name))
        if eq and value <= 0:
            raise ValueError("{} must be > 0".format(name))
        elif not eq and value < 0:
            raise ValueError("{} must be >= 0".format(name))

    def area(self):
        '''computes area of the rectangle'''
        return self.width * self.height

    def display(self):
        '''prints representation of the rectangle'''
        s = '\n' * self.y * \
            (' ' * self.x + '#' * self.width + '\n') * self.height
        print(s, end='')

    def __str__(self):
        '''returns string information about the rectangle'''
        return '[{}] ({}) {}/{} - {}/{}'.\
                format(type(self).__name__, self.id, self.y, self.x, self.width, self.height
