# 4. Recursion in Python

# 1 - Write a recursive function factorial(n) that returns the factorial of a number.

def factorial(n):
    if n == 0 or n == 1:   # Base case of recursion.
        return 1

    return factorial(n - 1) * n

print(factorial(4))
print(factorial(5))
print(factorial(6))