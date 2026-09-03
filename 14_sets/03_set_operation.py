# Set Operations: you can use different operations to perform on sets.

a = {3, 23, 53, 1}
b = {66, 11, 23, 1, 53}

c = a.union(b)   # Combine and print all the elements that are present in both a and b.
print(c)

c = a.intersection(b)   # Only print those elements that are common in both a and b.
print(c)

c = a.difference(b)   # It differentiates between a and b, and print the elements that are in a but not in b.
print(c)
