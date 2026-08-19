# 2 - Write a function safe_divide(a, b) that returns the result of a / b, but returns "Cannot divide by zero" if b is 0.

def safe_divide(a, b):
    if (b==0):
        return "Cannot divide by zero"
    else: 
        div = a / b
        return div

divide_1 = safe_divide(50, 5)
print(divide_1)

divide_2 = safe_divide(50, 0)
print(divide_2)