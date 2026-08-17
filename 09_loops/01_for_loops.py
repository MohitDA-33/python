# for loop ? for loops are used to iterate over a sequence(ex- string, list, range), a for loop executes a block of code repeatedly for each item in a sequence.

# To handle repetitive tasks in python we use loops

# Examples: a very few basic ones

print(1)
print(2)
print(3)
print(4)
print(5)

# This is a small example. Printing numbers from 1 to 5 is easy,
# but imagine printing numbers from 1 to 1,000,000.
# That's where loops become useful.

# Print 1 to 5
for i in range(1, 6):
    print(i)

# Why 6?
# Because range(start, stop) includes the start value
# but excludes the stop value.
# So range(1, 6) prints 1, 2, 3, 4, 5.

# Print the multiplication table of 17.
for i in range(1, 11):
    print("17 x",i,"=",17*(i))

# Counting from 1000 to 2000
for i in range(1000, 2001):
    print(i)