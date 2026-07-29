# Indexing and Slicing

# name = "Mohit"
# print(name[0])   We all know what it will print

name = "Mohit"
print(name[0:2])   #It goes from 0 to (2-1) = 1, just like range function goes from n to n-1. but its a positive indices.

# Now what about if we incorporate negative indices.
a = "Hello Python!"
print(a[3:-3])   #It will print (lo to pyth), its same as (3 to 10).

# Note: you can convert the negative to positive indices.

# Examples:

x = "Mohit0123456789"   #Total 15 characters in this string.
print(x[0:5])
print(x[0:15:1])   #Skip n-1 character, so it skips 0 characters cause 1 - 1 = 0.
# slicing syntax = (start:stop:step) 
print(x[0:15:2])   #skips 1 character 2 - 1 = 1

z = "Hello!"
print(z[0:])   #Replace the second empty number with the lenght(6) in this case.
print(z[:6])   #Replace the first empty number with 0.

# Few more examples:

f = "Python"
print(f[0])   #Output P
print(f[1])   #Output y
print(f[-1])   #Output n
print(f[-2])   #Output o

g = "Hello, Python!"
print(g[0:5])   #Hello
print(g[:5])   #Output same as (0:5)
print(g[7:])   #Python!
print(g[::2])   #Hlo Pto!
print(g[-6:-1])  #ython

h = "Python Programming"
print(h[::2])   # Output: Pto rgamn
print(h[::-1])   # Output: gnimmargorP nohtyP (reverses string)

message = "Welcome to Python!"
print(message[:7])   # Output: Welcome
print(message[-7:])   # Output: Python!
print(message[3:-3])   # Output: come to Pyt