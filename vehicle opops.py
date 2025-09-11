# Write a Python program to implement Inheritance by creating a Parent Class Vehicle with a constructor that has details like name, maximum speed, and mileage. Then, create a Child Class Bus that inherits Class Vehicle. Finally, showcase Inheritance to display the details of the Vehicle Bus named - School Volvo.
# parent class:-
class vehicle():
    def __init__(self,name,maximum_speed,mileage):
        # inicializing the variable
        self.name=name
        self.maximum_speed=maximum_speed
        self.mileage=mileage
class Bus(vehicle):
    pass
school_bus=Bus("School Volvo",250,20)
print("Vehicle name=",school_bus.name)
print("maximum speed=",school_bus.maximum_speed)
print("mialege=",school_bus.mileage)