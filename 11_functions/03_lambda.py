# Lambda functions

# We use lambda functions when we want to create a one-liner function, or whenever we want to define simple functions, or pass a function to a function.

# Example

square = lambda x: x*x   # (1) One liner, using lambda function
print(square(3))

def square(x):   # (2) Otherwise you have to write code this long enough.
    x = x*x
    return (x)  
print(square(3))

# Another examples:

add = lambda x, y: x+y   # (1)
print(add(15, 60))

def add(x, y):   # (2)
    z = x+y
    print(z)
add(98, 2)


average = lambda x , y, z: (x+y+z)/3   # (1)
print(average(x=21, y=8, z=1))

def average(x, y, z):   # (2)
    a = (x+y+z)/3
    print(a)
average(16, 11, 3)


quotient = lambda x, y: x%y   # (1)
print(quotient(100, 5))

def quotient(x, y):   # (2)
    a = x%y
    return(a)
print(quotient(50, 4))