# Break, continue and pass statments

# # The break statement is used to immediately exit a loop when a certain condition is met.

# Example:

for i in range(1, 11):
    if i == 7:
        break # cancel the execution of this loop now.
    print(i)

# So, what really happened here is when this loop runs it will start from i = 1, and then i = 2, its goes in a loop of iteration, but when it reaches number == 7, it enters the if statement i == 7, execute the break statement, and immediately exits the loop.

# Another example:

for i in range(21, 0, -1):
    if i == 10:
        break
    print(i)

# What it will do is it will start the loop iteration from 21, going backwards and when it reaches 10 it will halt the execution in between and will not print 10, it will print 11

for character in range(1, 11, 1):
    if character == 6:
        break
    print("*"*character)