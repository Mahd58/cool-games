# Write a program to create a base class Bird, with a constructor and two methods. Then, create a child class that inherits the constructor from Class Bird and has two functions. Finally, display how you can use Super to access the parent class constructor inside the child class.
class Bird():
    def __init__(self):
        print("Bird is ready")
    def swim(self):
        print("I can swim!")
    def who_is_this(self):
        print("I am a bird")
class penguin(Bird):
    def __init__(self):
        super().__init__()
        print("penguin is ready")
    def run(self):
        print("I can run!")
    def who_is_this(self):
        print("I am a penguin")
pingu=penguin()
pingu.who_is_this()
pingu.swim()
pingu.run()
