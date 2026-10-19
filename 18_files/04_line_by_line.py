# If you want to read the file, line by line for that you can use a for loop.

f = open("Introduction.txt", "r")
for line in f:   # Here a for loop is created that will print the file line by line.
    print(line.strip())   # .strip, removes all the whitespaces and newlines from the start and the end not from the middle.
f.close()


file = open("Credentials.txt", "r")
for line in file:
    print(line.strip())
file.close()

# If run - the files above are read line by line.