# Use of with statement.

# An advantage of using it- it closes the file itself even if there is an error, you don't have to manually do it.


# Read operation using with statement.

with open("Introduction.txt", "r") as file:
    show = file.read()
    print(show)


# Write operation using with.

with open("Credentials.txt", "w") as f:
    f.write("Yahoo- Hello@yahoo.com\n")
    f.write("*****")


# Append operation.

with open("Credentials.txt", "a") as f:
    f.write("\nThis is an appended line, end of program.")


# Use of for loop with (with).

with open("Credentials.txt", "r") as f:
    for line in f:
        print(line.strip())
