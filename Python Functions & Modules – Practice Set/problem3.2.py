# 2 - Create a list [1, 2, 3, 4, 5] and use map() with a lambda function to get their squares.

squares = lambda x: x*x
list1 = [1, 2, 3, 4, 5]

print(list(map(squares, list1)))

# OR 

list2 = [1, 2, 3, 4, 5]
print(list(map(lambda x: x*x, list2)))