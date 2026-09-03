# Set Methods: by using set methods you can add a new element or remove an existing element.

set = {34, 23, 1, 3, 22}
print(set)

set.add(5)   # .add, adds the element in the set.
print(set)

set.remove(23)   # .remove, removes the element from the set.
print(set)

set.pop()   # .pop, removes a random element from the set.
print(set)

set.discard(4343)   # .discard, removes the element from the set only if its present otherwise it will not show an error like remove shows, if a element doesnt exist in the set and if you try to remove it, it shows an error.
print(set)