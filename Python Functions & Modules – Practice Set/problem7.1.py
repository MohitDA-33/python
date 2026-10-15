# 7. Bonus Challenges

# 1 - Write a recursive function fibonacci(n) that prints the first n Fibonacci numbers.

def fibonacci(n):
    if (n == 0 or n == 1):
        return n

    return fibonacci(n-2) + fibonacci(n-1)

n = 6
for i in range(n):
    print(fibonacci(i), end = " ")