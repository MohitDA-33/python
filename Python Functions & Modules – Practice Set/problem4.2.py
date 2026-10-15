# 2 - Write a recursive function sum_of_digits(n) that returns the sum of all digits of a given number.

def sum_of_digits(n):
    if n == 0:   # Base case for recursion.
        return 0 

    return n%10 + sum_of_digits(n//10)   # dividing n by 10 and then + this will give me the number with last digit chopped of.

print(sum_of_digits(125))