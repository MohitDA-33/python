# Overloading, means giving an operator a special meaning for your own class objects.
# Example python knows that + operator adds number but it doesn't know how to add class objects for that we use overloading. 

class Number:

    def __init__(self, value,):
        self.value = value


    def __add__(self, other):   # __add__ is a special method that python uses when it sees a + operator.
       return self.value + other.value

num1 = Number(10)
num2 = Number(19)
print(num1 + num2)   # It will throw an error saying: TypeError: unsupported operand type(s) for +: 'Number' and 'Number'. # Edit: now it will not throw an error the comment was added written before  using  __add__.
'''
Here:
self = num1
other = num2
self.value = 10
other.value = 19
output = 29
'''

class String_X:

    def __init__(self, string):
        self.string = string

    def __add__(self, other):
       return  self.string + other.string

string_1 = String_X("Hello ")
string_2 = String_X("World")
print(string_1 + string_2)
'''
Here:
self = string_1
other = string_2
self.string = "Hello "
other.string = "world"
output = Hello world
'''

class Multi:

    def __init__(self, multiply):
        self.multiply = multiply

    def __mul__(self, other):
       return  self.multiply * other.multiply

N1 = Multi(15)
N2 = Multi(5)
print(N1 * N2)
'''
Here:
self = N1
other = N2
self.multiply = 15
other.multiply = 5
output = 75
'''