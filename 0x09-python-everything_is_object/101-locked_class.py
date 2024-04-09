"""a class that prevents the user from creating new instances with an exception"""


class LockedClass:
    """class with no object"""
    __slots__ = ('first_name', )  # declare allowed attr

    def __setattr__(self, name, value):
        """function to set attrtibute"""

        if hasattr(self, name):
            super().__setattr__(name, value)
        elif name == 'first_name':
            super().__setattr__(name, value)
        else:
            raise AttributeError("Can't create instance")
