# Variable scope and Docstrings

'''
Scope: in python variables have scope (where they can be accessed or not).

Lifetime: python lifetime defines how long they exist or how long the variable exists
'''

def sum(a, b):   # a and b are here local variable, you can access these variable inside a function only.
    c = a + b
    z = 1   # It creates a local variable called z which is destroyed after this function returns, so if you try to print(z) it will z = 8 and not z = 1.
    return c

z = 8   # I can access this from anywhere, cause its a global variable.
print(sum(10, 6))
# print(c) If you try to execute this it will show an error cause when a function is called and they return the value, the variables gets destroyed immediately. so variable are created when a function is called and gets destroyed when it returns.
print(z)

# There are 2 types of scope in python: local scope and global scope.

# Example: of local variable

def greet(name):
    z = 23   # Local variable
    return f"Hello {name}"

print(greet("mohit"))


# Another example:

x = 10  # Global variable

def my_func():
    x = 5  # Local variable
    print(x)  # This will give you the output 5.

my_func()
print(x)  # and this will give you the output 10.1 
