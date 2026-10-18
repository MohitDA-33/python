# Read, Write, and Append files in python.

# There is a file name- Introduction.txt and we will try to do read operation on it.

# To read we need to create a file object.

f1 = open("Introduction.txt", "r")
# r stand for read. remember that the actual is rt and its default, t stands for text. and other is rb, b stand for binary.

content = f1.read()   # Content is a variable created that will store the content of the file.
print(content)   # And print will print the content.

f1.close()


# Another example.

f2 = open("Credentials.txt", "rt")

show = f2.read()
print(show)

f2.close()
