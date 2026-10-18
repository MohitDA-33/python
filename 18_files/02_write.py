# Question --> Write to file name john_doe.txt, And it should contain information about john doe.


f = open("john_doe.txt", "w")
# w stands for write operation, remember if the file already exists the content inside will be overriden and if not, a new file will be created.

content = '''Hi my name is John doe
i live in nyc, and i work in meta.'''
# We created a variable here which contains a string, and this string will get added to the file.
f.write(content)   # It will write the content of the content in the file- john doe.txt.

f.close()


'''
# Now if we want we can again open the file and read it, but its optional.

f = open("john_doe.txt", "rt")

show  = f.read()
print(show)

f.close()
'''

'''
# Another way of writing...

file = open("john_doe.txt", "w")
file.write("Hello!, my name is John doe.\n")
file.write("I live in nyc and i work in meta.\n")
file.close()
'''