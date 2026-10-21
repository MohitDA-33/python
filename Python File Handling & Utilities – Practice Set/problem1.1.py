# 1. File I/O Basics

# 1 - Create a text file notes.txt using Python and write "Learning Python is fun!" into it.

file = open("notes.txt", "w")
file.write("Learning Python is fun!")
file.close()


'''
# Use of with statement to solve it.

with open("notes.txt", "w") as file:
    file.write("Learning Python is fun!")
'''