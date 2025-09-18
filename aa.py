# Write a program to create a base class that consists of two functions - one to display a value, and another function is an abstract method. Next, create a subclass that consists of a method similar to the abstract method. Finally, showcase how Abstraction is being implemented in this example.
#base class means parent class and sub class means child class
from abc import ABC,abstractmethod
class base(ABC):
    def __init__(self):
        super().__init__()
    def display(self):
        print("i am the display function")
    @abstractmethod
    def task(self):
        print("i am the abstractn method")
class child(base):
    def __init__(self):
        super().__init__()
    def task(self):
        print("i am in the child class")
ob1=child()
ob1.display()
ob1.task()