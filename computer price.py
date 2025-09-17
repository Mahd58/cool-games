# Write a program to create a class Computer with a private attribute max_price and methods sell(to display) the selling price and setmaxprice(change the private attribute max_price). Now create an object for the class Computer. Try changing the value of max price and use the sell function to display the updated price. Use a setter function to update the value and again display the price.
class computer():
    def __init__(self):
        self.__maxprice=7
    def sell(self):
        print(self.__maxprice)
    def set__maxprice(self,price):
        self.__maxprice=price
c=computer()
c.sell()
c.set__maxprice(1000)
c.sell()
