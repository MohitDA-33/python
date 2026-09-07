# 3- Convert the tuple to a list, change its first element to 50, and convert it back to a tuple.

coordinates = (10, 20)   # I know that tuples are immutable, so we cannot change the values.

list_cor = list(coordinates)   # First we typecasted the tuple in a list.
list_cor[0] = 50   # Then we changed the value to --> 50.
print(list_cor)

new_coord = tuple(list_cor)   # And then again we typecast it to a tuple. 
print(new_coord)