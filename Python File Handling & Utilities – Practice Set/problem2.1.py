# 2. Read, Write, and Append Files

# 1 - Write a program that writes three lines of text to a file tasks.txt.

f = open("tasks.txt", "w")
f.write("1- Solve 12 questions.\n")
f.write("2- Complete 2 lessons of sql.\n")
f.write("3- Revise past 7 sections of python.")
f.close()

# Another way of doing it

f = open("tasks.txt", "w")
script = '''1- Solve 12 questions.
2- Complete 2 lessons of sql.
3- Revise past 7 sections of python.'''
f.write(script)
f.close()

'''
# Use of with statment to answer it.
with open("tasks.txt", "w") as f:
    f.write("1- Solve 12 questions.\n")
    f.write("2- Complete 2 lessons of sql.\n")
    f.write("3- Revise past 7 sections of python.")
'''