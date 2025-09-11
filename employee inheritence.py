# Write a program to create a parent class Person (attributes - name, id number) with a method display to display the attributes. Next, create a child class Employee (attributes - name, id number, salary, post). Access the attributes of parent class in child class. Then, create an object for child class and call the display method to display the name and id number.
class Person():
    def __init__(self,name,id_number):
        self.name=name
        self.id_number=id_number
    def display(self):
        print(self.name)
        print(self.id_number)
class Employee(Person):
    def __init__(self,name,id_number,salary,post):
        self.salary=salary
        self.post=post
        # ewaking init from parent class
        Person.__init__(self,name,id_number)
E1=Employee(name="Mahd",id_number="777",salary=15000,post="intern")
E1.display()