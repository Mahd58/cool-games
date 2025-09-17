# Write a program to create a class with following variables and methods - 1. Private variable named privateVar that contains an integer value 2. Create a private function privMeth that prints a message 3. Create a function hello that prints the value of privateVar 4. Create an object for the class and call all the functions.
class myclass():
    __privateVar=7,7,7,7
    def __privMeth(self):
        print("I have a world record of never eating from canteen")
    def hello(self):
        print("__privateVar")
s1=myclass()
s1.hello()
s1.__privMeth()