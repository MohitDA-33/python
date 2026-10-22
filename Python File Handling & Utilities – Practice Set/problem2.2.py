# 2 - Open tasks.txt in append mode and add a new line "Task Completed!".

f = open("tasks.txt", "a")
f.write("\nTask Completed!")
f.close()


# Another way of doing it

'''
f = open("tasks.txt", "a")
string = "\nTask Completed!"
f.write(string)
f.close()
'''

'''
# Using with to solve.
with open("tasks.txt", "a") as f:
    f.write("\nTask Completed!")
'''