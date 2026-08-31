def sum(a, b):
    '''This will sum 2 numbers'''
# It might look like regular pyhton comment, but if you write it inside a function its called doc-strings.
    c = a + b
    return c

print(sum(10, 5))
print(sum.__doc__)   # It will print the information in triple quotes, this information is called docstrings.

# Doc-strings are used to attach an information about the function. ex: if someone is using your function as a module and you want to give him the information, or kind of documentation on how to use this function and what this function is.


# Note: its better to write the doc-strings in a proper way, so that if someone else is using your function they can understand easily what this function does.

# Example:

def add(a, b):
    """
    Returns the sum of two numbers.

    a: The first number.
    b: The second number.

    Sum both of them and stores the value in c.
    And then c is returned back to us.
    """
    c = a + b
    return c 

print(add(20, 19))
print(add.__doc__)
