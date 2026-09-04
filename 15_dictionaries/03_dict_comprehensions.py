# Dictionary comprehensions, is a way of creating quick dictionary.

# Example, creating a table of 9 with numbers, like 1-->5 , 2-->10 and so on..

dct = {i: 5*i for i in range(1, 11)}
print(dct)

# Another example: Square

sqr = {i: i**2 for i in range(1, 6)}
print(sqr)

# Cube

cube = {i: i**3 for i in range(1, 6)}
print(cube)
