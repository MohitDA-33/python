# Tuples and Operations on Tuples

# Tuples: tuples are ordered just like lists but they are immutable(cannot be changed after creation).

tu_1 = (11, 22, 39, 34, 55, 61, 67)   # In order to create a tuple we use paranthesis, and in list we use square brackets.
print(tu_1)

tu_2 = (9,)   # To create a tuple with one element, the comma is required. in list you can simply write tu_2 = [9].
print(tu_2)

# Accessing elements/objects in a collection: to access elements we can use indexing and string slicing.
print(tu_1[1])
print(tu_1[3])
print(tu_1[3:])
print(tu_1[-7:])
print(tu_1[0:7])

'''
If you try to change the elements/objects it will show an error, cause tuples are immutables. example

tu_1[0] = 12
print(tu_1[0])
'''