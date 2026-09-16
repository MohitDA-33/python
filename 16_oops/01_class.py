'''
Class and Object

Class, class is a blueprint or template eg- form for an exam that contains name, age, electives, fathers and mothers name.

Object, specific instance created from the template(class) eg. form which contains the data of john doe.

Actions performed in the class is class methods and class will have data thats called attributes.
data --> attributes and methods --> functions.
'''
class user_info:   # user_info is a class or a blueprint for creating an object.
    name = input("Enter your name: ")   # And these are the class attributes(data).
    age = input("Enter your age: ")
    electives = input("Enter your electives: ")
    fathers = input("Enter your fathers name: ")
    mothers = input("Enter your mothers name: ")

employee_1 = user_info()   # employee_1 is an object made from the class user_info().
print(user_info.name)
print(user_info.age)
print(user_info.electives)
print(user_info.fathers)
print(user_info.mothers)   

# employee_1 --> is an object made from the class --> user_info(), but these attributes (name, age, electives...) belong to the class.

employee_2 = user_info()   # employee_2 is an object made from the class user_info().
print(user_info.name)
print(user_info.age)
print(user_info.electives)
print(user_info.fathers)
print(user_info.mothers)  

employee_3 = user_info()   # employee_3 is an object made from the class user_info().
print(user_info.name)
print(user_info.age)
print(user_info.electives)
print(user_info.fathers)
print(user_info.mothers)


# Another example:

class employee():   # Here class is an employee.
    company = "HP"   # This is a class attribute.

    def get_salary(self):   # And this is a class methods.
        print(self)   # This will print the memory location of the objects that are calling this function.
        return 35000

e1 = employee()   # e1 is an object made from class(employee()).
print(e1.get_salary())
print(e1.company)

e2 = employee()   # e2 is an object made from class(employee()).
print(e2.get_salary())
'''
Self, basically references to the object which is being talked about, any object i am creating if i want to refer i can refer it using self.

So whenever i run get_salary function for e1, self is basically e1 and same for e2.

And its mandatory to give first parameters as self for all the functions we are defining.
'''