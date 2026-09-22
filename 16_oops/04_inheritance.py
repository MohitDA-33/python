# Inheritance, is like a family tree where the child inherits the traits from parent class but in python the class child inherits all the attributes and methods that a parent class has.

# Animal is a parent class.

class Animal:

    location = "Australia"   # A class Attribute.

    def __init__(self, name):
        self.name = name   # A constructor that creates an instance variable and assign a value to name when given.

    def speak(self):
        print("Speaking now")

# While Dog is a child class that have all the traits inherited from parent class.

class Dog(Animal):   # This is how inheritance is done, Class [Dog] will have all the traits of class (animal) or simply, now class [Dog] will have all the attributes and methods that class [Animal] has. 
    def speak(self):   # This is called methods overridden, how ? we have overriden the method speak() in class [Animal], with the its child class [Dog].
        super().speak()   # Call the method of parent class, we are using speak() function of the parent class.
        print("Woof!")

# a = Animal("Dog")
# a.speak()
# print(a.location)

b = Dog("Jimmy")
b.speak()

# super() methods, is a method to call parent class.
