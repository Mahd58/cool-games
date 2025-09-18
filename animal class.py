# Write a program to implement abstraction on animal class (base class). The abstract method will be move will display what subclasses can do. Subclasses can be something like - Human, Dog.
from abc import ABC,abstractmethod
class animal(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def move(self):
        pass
class cub(animal):
    def __init__(self):
        super().__init__()
    def move(self):
        print("i can walk")
class snake(animal):
    def move(self):
        print("I can crawl")
class bird(animal):
    def move(self):
        print("I CAN FLY!!!!!!!!!!!!!!!!!!!!!")
one=cub()
one.move()
two=snake()
two.move()
three=bird()
three.move()