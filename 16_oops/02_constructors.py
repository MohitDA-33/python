# Constructors in python, we use constructors to initialze our objects.

class employee():   # Employee() is a class.

    def __init__(self, salary, name, bond):   # when we write __init__ this creates a constructor, and this will take some parameters and initialize our objects with those parameters.
        self.salary = salary   # Create an instance attribute of name salary and assign it with a salary.
        self.name = name   # " "...
        self.bond = bond   # " "...
# So basically we are setting an instance attribute called salary, name and bond with thier values 37000, "John", 3.

    def get_salary(self):
        return self.salary
    
    def user_info(self):
        print(f"Hi, {self.name} nice to meet i know for how many years you are going to work, its {self.bond}")

e1 = employee(37000, "John", 3)
print(e1.get_salary())  
'''
It will give me the salary that i have set for e1 = 37000, if salary is running means its for e1.
So self.salary basically means we are referring to the object for which that function is running.  
'''

# This is a constructor and whenever we write __init__ it means the constructor and its used to initialize objects.
e1.user_info()


# Another example:

class dogs():

    def __init__(self, name, breed, size):
        self.name = name
        self.breed = breed
        self.size = size

    def dog_name(self):
        print(self.name)

    def dog_breed(self):
        print(self.breed)

    def dog_size(self):
        print(self.size)

dog_1  = dogs("orco", "Labrador", "Medium")
dog_1.dog_name()
dog_1.dog_breed()
dog_1.dog_size()

dog_2  = dogs("Joy", "Beagle", "small")
dog_2.dog_name()
dog_2.dog_breed()
dog_2.dog_size()