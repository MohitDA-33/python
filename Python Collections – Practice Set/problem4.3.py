'''
3- Create two sets:

a = {1, 2, 3}

b = {3, 4, 5}
Find their:

Union

Intersection

Difference (a - b)
'''

a = {1, 2, 3}
b = {3, 4, 5}

c = a.union(b)   # Combine all the elements that are in a as well as b.
print(c)

d = a.intersection(b)   # Print only those elements that are common in both a and b.
print(d)

e = a.difference(b)   # Will print only those elements that are present in a and not in b.
print(e)