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

    @classmethod
    def save_to_file(cls, list_objs):
        '''method that wites the JSON rep of list_objs'''
        json.dumps(list_objs)
        Base(list_objs)

        if list_objs is not None:
            list_objs = [o.to_dictionary() for o in list_objs]
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        '''method that returns the list of JSON string representation'''
        if json_string is None or not json_string:
            return []
            return json.dumps(json_string)
    
    @classmethod
    def create(cls, **dictionary):
        '''method that returns an example with all attributes'''
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            new = Rectangle(1, 1)
        elif cls is Square:
            new = Square(1)
        else:
            new = None
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        '''method that returns instances'''
        from os import path
        file = "{}.json".format(cls.__name__)
        if not path.isfile(file):
            return []
        with open(file, "r" encoding="utf-8") as f:
            return [cls.create{**d} for d in cls.from_json_string(f.read())]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''methods that deserialize and serialize'''
        from models.rectangle import Rectangle
        from models.square import Square
        if list_objs is not None:
            if cls is Rectangle:
                list_objs = [[o.id, o.width, o.height, o.x, o.y]
                            for o in list_objs]
            else:
                list_objs = [[o.id, o.size, o.x, o.y]
                            for o in list_objs]
        with open('{}.csv'.format(cls.__name__), 'w', newline='',
                encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        '''methods that deserialize and serialize'''
        from models.rectangle import Rectangle
        from models.square import Square
        ret = []
        with open('{}.csv'.format(cls.__name__), 'r', newline='',
                encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                row = [int(r) for r in row]
                if cls is Rectangle:
                    d = {"id": row[0], "width": row[1], "height": row[2],
                            "x": row[3]. "y": row[4]}
                else:
                    d = {"id": row [0], "size": row[1],
                            "x": row [2], "y": row[3]}
                    ret.append(cls.create(**d))
                return ret

    @staticmethod
    def draw(list_rectangles, list_squares):
        '''method that opens a window all rectangles and squares.'''
        import turtle
        import time
        from random import randrage
        turtle.screen().colomode(255)
        for i in list_rectangle + list_squares:

