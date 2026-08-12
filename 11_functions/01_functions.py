# Functions in python

# We are trying to get an average of 3 numbers.

a = 10
b = 19
c = 55

d = (a + b + c)/3
print(d)

# Its a small program if i have to change the values or say i want to change the approach i have to change it everywhere
# In this case there are only few lines of programs what about 50 or more, i have to write the whole program again.

a1 = 19
b1 = 75
c1 = 85

d1 = (a1 + b1 + c1)/3
print(d1)

# Functions help us here : (Functional approach)

# To create a function we use (def) keyword, any function starts with the def keyword.

def average(a, b, c):
    d = (a + b + c)/3
    print(d)

average(10, 15, 25)
average(19, 18, 97)

# We can assign/change value as many times as possible.

# Another example:

def text(name):
    print(f"Hello!, {name} nice to meet you")

text("Mohit")
text("Aditi")

# Return statement: returns the value/output after the computation or when function has been executed, so that you can use that value/output later or can store that.

def avg(a, b, c):
    x = (a + b + c)/3
    return (x)

m1 = avg(10, 5, 15)
print(m1)

# Another example:

def greet(name, age):
    return f"Hi {name}, your age is {age}"

n1 = greet("Mohit", 22)
print(n1)   