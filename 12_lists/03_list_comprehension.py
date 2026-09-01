# list comprehension: is the way of creating quick lists.

# Example: i want to create a list containing the table of 5.

table_5 = []
for i in range(1, 11):
    table_5.append(5 * i)   # It will append the the table of 5 inside the list.

print(table_5)   # And after appending we are printing the table, that was empty in the first hand.

# But still as you can see its a code with lot of lines, why not make it small or create a shortcut.

table_5 = [5 * i for i in range(1, 11)]
print(table_5)

# Another example:

square = []

for i in range(1, 6):
    square.append(i ** 2)

print(square)

square = [i ** 2 for i in range(1, 6)]
print(square) 