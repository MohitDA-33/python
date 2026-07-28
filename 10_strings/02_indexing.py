# String indexing

# NOTE: counting in programming starts with 0.

# Every character in a string has an index. positive and negative index/indices.

# Positive indices/index
y = "Hello"
print(y[0])
print(y[1])
print(y[2])
print(y[3])
print(y[4])

# The first letter of the character starts with 0, in this case its H, 1 = e, 2 = l and so on... and what if i write 5, it will show error cause the string is not that long enough

# Negative indices/index

# It starts with -1 and it also start with the last letter of the character.[-1] = in this case t, [-2] = i, and so on...

z  = "Mohit"
print(z[-5])
print(z[-4])
print(z[-3])
print(z[-2])
print(z[-1])

# To convert negative to positive, you add the size of the string in both the cases its 5, to the negative index, ex = -4, -4+5 = 1, so -4 = o and 1 = o, if we take the above example (Mohit).

a = "!@#$%"
print(a[0])   # Prints !
print(a[-1])   # Prints %
print(a[-3])   # Prints #
print(a[2])   # Prints #