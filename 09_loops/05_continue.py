# It is very similar to break statement but its a bit different.

# So, what continue statement does is, its start printing the iteration loop as given, and when it enters the if statement, it will skip the current iteration of the loop and moves directly to the next iteration. skipping the current value.

# Example:

for i in range(1, 11, 1):
    if i == 5:
        continue # continue the loop for the next iteration here itself.
    print(i)

# Another examples:

for character in range(1, 6, 1):
    if character == 2:
        continue
    if character == 4:
        continue
    print("$"*character)


for i in range(20, 10, -1):
    if i == 15:
        continue
    print(i)