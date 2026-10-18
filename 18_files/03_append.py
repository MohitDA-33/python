file = open("john_doe.txt", "a")   # a stands for append. which will append the data in the file.
file.write("Hello! Python.\n")
file.write("Hello! World.\n")
file.close()

# Another way of writing...

f = open("john_doe.txt", "a")
string = "This line will get appended in the end of the line."
f.write(string)
f.close()

# Remember if the file does not exist and you are trying to append, a new file will be created. and every time you run, the data/content will get append everytime.