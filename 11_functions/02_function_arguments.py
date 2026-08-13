# Function arguments and return values

# 1 - Postional argument

def add(a, b):
    x = a + b
    print(x)

add(3, 5)

# The values/arguments 3 and 5 are passed to a & b in a order, matched by position, So 3 as a and 5 as b after the computation the output is returned back.

def greet(name, age):
    print(f"Hi {name}, you are {age} years old.")

greet("Mohit", 22)

# 2 - Keyword argument

def plus(c ,d, e):
    y = (c + d + e)/3
    print(y)

plus(c=17, d=3, e=10)

# The values/arguments are defined to the values of thier exact parameters, so you can write them in any order without thinking about the position.

def hello(name, language):
    print(f"Hi i am {name} and i like {language} programming language")

hello("Mohit", "Python")

# 3 - Default arguments

def average(a, b, c=0):
    z = (a + b + c)/3
    print(z)

average(15, 5, 10)

# Here c comes with a default value 0, it used when the caller doesnt provide the value/argument. and if the caller provides a value the default value will be overridden.

def intro(study, height, guest="Mohit"):
    print(f"Hi {guest}, you study in {study} and your height is {height}m")

intro(study="B.com", height=1.778, guest="Aditi")