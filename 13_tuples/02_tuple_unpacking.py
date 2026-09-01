# Tuple unpacking: where we assign variable/s with the element/s of a tuple. example

# So whats happening here is:
tu = (51, 91, 1)   # Here we have created a tuple.
a, b, c = tu   # We are assigning these variables a, b, c to the elements of the tuple, so now a = 51, b = 91, c = 1.
print(a, b, c)   # And now we are printing the variables.

# What if there were 4 elements instead of 3, like(51, 91, 1, 3) the above example would have shown error, it will expect 3 elements to be there cause there are 3 variables, it will expect 3 and get 4 to unpack.

# Another example:

tuple = (79, 89, 91)
tu_1, tu_2, tu_3 = tuple
print(tu_1, tu_2, tu_3)
print(tu_1)
print(b)
print(c)
print(tu_2)