# 3 - Read the file and print all lines as a list using readlines().

file = open("tasks.txt", "r")
show = file.readlines()
print(show)
file.close()

'''
# Answering it using with statment.
with open("tasks.txt", "r") as file:
    show = file.readlines()
    print(show)
'''