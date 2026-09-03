# Sets and Set Methods

# Set, a set is a collection of unordered elements where the elements cannot be repeated(no duplicates).

s = {3, 23, 13, 16, 31}
print(s)
print(s, type(s))   # You can also print the type of objects, use type().
# print(s[3])   If you try to access an element it will show and error, cause sets are unordered.
# print(s[0:])   The same will happen with the slicing too.

set_1 = {10, 20, 30, 40, 50, 50, 40}   # If you try to give multiple of the same element it will only, ex-1 in this case there are two (50) but it will only print one instead of two.
print(set_1)
