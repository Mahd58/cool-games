# Write a program to create a class Parrot and perform the following tasks - 1. Create a class variable species 2. Create a __init__ method that has instance variables - name and age 3. Create instances of class Parrot, passing arguments as well 4. Print Class variable by accessing it 5. Print Instance variables as well
class parrot:
    # class variable
    species="birds"
    def __init__(self,name,age):
        # instance variable
        self.name=name
        self.age=age
P1=parrot("oh mitho",4)
print(P1.name)
print(P1.species)