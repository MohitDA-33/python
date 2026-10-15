# 6. Variable Scope and Docstrings

# 1 - Write a function increment() that has a local variable counter initialized to 0 and increments it by 1 each time it is called. Observe whether the value persists across function calls.

def increment():
    counter = 0
    counter += 1
    print(counter)

increment()   # output: 1 1 1 
increment()
increment()

# Its an observation question on how local variable behaves, it teaches you that variable is fresh everytime the function is called.