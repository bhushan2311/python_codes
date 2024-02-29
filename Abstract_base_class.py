# import abc
from abc import ABC, abstractmethod
# class Shape(abc.ABC):
class Shape(ABC):
    # @abc.abstractmethod
    @abstractmethod          # this tells, you must define its method in its child class/es
    def area(self):
        return 0
    pass

class Rectangle(Shape):

    def __init__(self,len,bre):
        self.length=len
        self.breadth=bre

    def area(self):          # defined abstract method
        return self.length * self.breadth
    pass

class Square(Shape):

    def __init__(self,len):
        self.length=len

    def area(self):         # defined abstract method
        return self.length * self.length
    pass

rect=Rectangle(3,2)
sq=Square(4)

print(rect.area())
print(sq.area())