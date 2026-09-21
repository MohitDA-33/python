'''
2. Constructor and Attributes

Create a class Person with a constructor (__init__) that accepts name and age as arguments and stores them as instance attributes.
Create an object and print the person’s name and age.
'''

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def person_name(self):
        print(f"The name of the person is {self.name}")

    def person_age(self):
        print(f"And the age is {self.age}")

p1 = Person("Mohit", 22)
p1.person_name()
p1.person_age()
