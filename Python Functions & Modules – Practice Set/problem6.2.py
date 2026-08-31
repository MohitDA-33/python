# 2 - Write a function multiply(a, b) that has a proper docstring explaining what it does. Then use help(multiply) to display the docstring.

def multiply(a, b):
    '''
    Returns the product of two numbers.
    a: The First number
    b: The Second number

    This function multiplies both number and
    Stores the value in x, and returns it to you.
    '''
    x = a * b
    return x

print(multiply(10, 19))
help(multiply)