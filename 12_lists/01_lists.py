# Lists in pyhton: lists are ordered and mutable collections of items.

# Examples of lists: suppose i want to write marks of 5 students, for that i have to create 5 different variables, rather i will create a lists.

marks = [89, 68, 73, 54, 91]   # Marks are of out 100.
print(marks)   # As lists are ordered, every time you print the list, it will print in the same order.

mix = [95, "Mohit", True, 199.99]   # Its a collection of string, float, boolean and integer.
print(mix)

# Can i access the elements of a list individually ? yes i can by using indexing.

print(marks[2])   # It will print 73, cause the index in python starts with 0.
print(marks[-4])   # Added an example of negative indices too, it will print 68.
print(mix[1])   # It will print Mohit.

# Can we do string slicing in a list ? yes i can

print(marks[1:5])   # Print from 68 to 91.
print(mix[-3:])   # Print Mohit, True, and 199.99.
print(mix[0:2])   # Print 95 and Mohit.