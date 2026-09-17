# Class and Instance attribute,

# Instance attribute, are specific to instance.
# class attribute, are specific to class.

class employee():

    company = "AMD"   # AMD is a class variable/attribute.

    def __init__(self, salary, name, bond, company):
        self.salary = salary
        self.name = name   # This is an instance attibute.
        self.bond = bond
        self.company = company

e1 = employee(39000, "John", 5, "Tesla")
print(e1.company)   # This will print the class attribute if we dont have the instance attribute.  # (After adding company as input) --> it will always print the instance attribute over class.

# What if i add company as an input here ? It will always print instance attribute whenever present.

# But how you can print the class attribute (company) ?

print(employee.company)   # This will always print the class attribute.


# Object introspection in python, is a way to find all the methods and attributes that a particular object has, we use [ dir ]method for that.

print(dir(e1))   # This will print all the methods and attributes that are in object (e1).