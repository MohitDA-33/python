def new(a, b):
    x = a + b
    global c   # It modifies the z into global variable, and it does not create a local variable.
    c = 30   # For now a local variable can be accessed within the function only.
    return x 

c = 3   # Its a global variable and can be used throughout the program from anyhwere, but ofcourse not inside a function.
print(new(19, 29))
print(c)

# But what if i want to update the global variable and i want to print c = 30 than c = 3, then i will use global keyword.


# Another example:

x = 10  # Global variable

def modify_global():
    global x   # Modifies the x from local to global 
    x = 5  

modify_global()
print(x)  # This will print 5 and not 10 cause the global variable has been changed.