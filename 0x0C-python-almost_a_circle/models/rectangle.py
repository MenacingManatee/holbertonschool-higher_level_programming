#!/usr/bin/python3
'''Defines the class Rectangle that inherits from Base'''
from models.base import Base


class Rectangle(Base):
    '''Defines a rectangle by width, height, position, and ID'''
    def __init__(self, width, height, x=0, y=0, id=None):
        '''initializes id, and calls setters of width, height, and pos'''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''Getter for width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Setter for width'''
        self.integer_validator("width", value)
        self.__width = value

    @property
    def height(self):
        '''Getter for height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Setter for height'''
        self.integer_validator("height", value)
        self.__height = value

    @property
    def x(self):
        '''Getter for position x'''
        return self.__x

    @x.setter
    def x(self, value):
        '''Setter for x'''
        self.integer_validator("x", value)
        self.__x = value

    @property
    def y(self):
        '''Getter for y'''
        return self.__y

    @y.setter
    def y(self, value):
        '''Setter for y'''
        self.integer_validator("y", value)
        self.__y = value

    def integer_validator(self, name, value):
        '''Validates integers for private values'''
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if name in ("width", "height") and value <= 0:
            raise ValueError('{} must be > 0'.format(name))
        if name in ("x", "y") and value < 0:
            raise ValueError('{} must be >= 0'.format(name))

    def area(self):
        '''Finds the area of a rectangle'''
        return self.__width * self.__height

    def strrep(self):
        '''Creates a string representation for returning or printing'''
        res = []
        res.append('\n' * self.__y)
        res.append(str(' ' * self.__x + "#" * self.__width + '\n') *
                   self.__height)
        return "".join(res)

    def display(self):
        '''Prints in stdout the Rectangle instance with the character #'''
        print(self.strrep(), end="")

    def __str__(self):
        '''overrides the __str__ method so that it returns:
        [Rectangle] (<id>) <x>/<y> - <width>/<height>'''
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.__x, self.__y,
                                                       self.__width,
                                                       self.__height)

    def update(self, *args, **kwargs):
        '''assigns an argument to each attribute
        Usage: update(self, id, width, height, x, y)'''
        if len(args) == 0:
            if 'id' in kwargs:
                self.id = kwargs.get('id')
            if 'width' in kwargs:
                self.width = kwargs.get('width')
            if 'height' in kwargs:
                self.height = kwargs.get('height')
            if 'x' in kwargs:
                self.x = kwargs.get('x')
            if 'y' in kwargs:
                self.y = kwargs.get('y')
            return
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.width = args[1]
        if len(args) > 2:
            self.height = args[2]
        if len(args) > 3:
            self.x = args[3]
        if len(args) > 4:
            self.y = args[4]

    def to_dictionary(self):
        '''returns the dictionary representation of a Rectangle'''
        res = {}
        res.update({"id": self.id})
        res.update({"width": self.width})
        res.update({"height": self.height})
        res.update({"x": self.x})
        res.update({"y": self.y})
        return res
