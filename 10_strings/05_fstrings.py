# String Formatting and f-string
# It allows you to insert variables and expressions into strings. there are multiple ways to format strings


# Older method = .format()

name = "Mohit"
height = 1.778
print("My name is {}, and i am {} meters tall" .format(name, height))

# Use of positional and keywords arguments
print("My name is {0}, and i am learning {1}".format("Mohit", "Python"))   # 0 = mohit, and 1 = python

# Few more example:
a = "mohit"
a1 = 10000
b = "aditi"
b1= 11000

print("hey {} you get {} $ for you work" .format(a, a1))
print("hey {} you get {} $ for you work" .format(b, b1))


x = 10 
y = 20
template = "sum of {} and {} is = {}"
print(template.format(x, y, x+y)) 


# New method introduced in python 3.6 = f-string (formatted string laterals) 
g = "Hello"
h = "Mohit"
print(f"{g} everyone my name is {h}")   # Its a simple way to put variables/expressions inside a string just put f in front of the string.

num1 = 19
num2 = 19
print(f"{num1} multiply by {num2} is {num1*num2}")

# Align text with f-string
name = "Mohit"
print(f"{name:<20}")   # left align in 20 spaces
print(f"{name:>20}")   # right align in 20 spaces
print(f"{name:^20}")   # center align in 20 spaces

# Control decimal places

pi = 3.14159265
print(f"pi = {pi:.2f}")   # 2f means show 2 digits after decimal point

# All the example's done in the .format() way can be done by using f-strings as well.