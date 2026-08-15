# Recursion in Python : Recursion occurs or happens when a function calls itself

# Example : fibonacci series is a series that starts with 0 and we keep adding the first 2 default numbers.
'''
0 1 1 2 3 5 8 13...   Fibonacci series
0 1 2 3 4 5 6 7...   Positive indices/index
'''

def fib(n):
    # Base case of recursion
    if(n==0 or n==1):   # First it goes to the base case, matches if its true, in this case no cause its 6 not 0 or 1, if its 1 or 0 it will return back, if not then
        return n 

    return fib(n-2) + fib(n-1)   # It comes here for the rest of the value, and compute it using the formula

print(fib(6))   # fib(6) (6 - positive index) is passed to the function

# Summary: when n=6 is passed to the function, the first case is false cause n==0 or n==1, so 2nd case is taken under. and the problem is broken down

'''
break down fib(6)
fib(6) = fib(n-2) + fib(n-1) 
fib(6) = fib(4) + fib(5)
fib(4) + fib(5)   [further break down} 
fib(2) + fib(3) + fib(4) + fib(3) 
fib(0) + fib(1) + fib(1) + fib(2) + fib(2) + fib(3) + fib(1) + fib(2) 
0 + 1 + 1 + fib(0) + fib(1) + fib(0) + fib(1) + fib(1) + fib(2) + 1 + fib(0) + fib(1)
0 + 1 + 1 + 0 + 1 + 0 + 1 + 1 + fib(0) + fib(1) + 1 + 0 + 1 
0 + 1 + 1 + 0 + 1 + 0 + 1 + 1 + 0 + 1 + 1 + 0 + 1 = 8 (fibonacci series no 8)
As you can see the index no 6, gives you fibonnaci series no 8 
'''

# Remember: if dont have a base case, you might can get stuck in a infinite loop. in my case if there is no base case the values would have gone to minus and keep computing tills my memory crashes.