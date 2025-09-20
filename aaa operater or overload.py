# Write a program to overload the less than (<) and equal to (==) operators. For example, create objects - ob1 and ob2 with values 3 and 4 to compare values, respectively. You can additionally create more objects to try different values.
class Random():
    def __init__(self,number):
        self.number=number
    def __lt__(self,other):
        if self.number<other.number:
            return "object 1 is less than object 2"
        else:
            return "object 2 is less than object 1"
    def __eq__(self,other):
        if self.number==other.number:
            return "both are equal"
        else:
            return "Both are not equal"
ob1=Random(13)
ob2=Random(50)
print(ob1<ob2)
print(ob1==ob2)