# Modules and pip - using external library

import math
print(math.sqrt(16))

'''
Import is a keyword in python that helps to import a module.
Here we have imported an in-built module math(), which helps you to perform mathematical operations
and we are using one of its function .sqrt which gives you the square root of a number. 
'''
print(math.pow(10, 3))
print(math.cbrt(1000))

# Another in-built module = os()

import os
print(os.getcwd())   # Tells you the current directory you are in.
print(os.listdir())   # Prints the content of the directory you are in.

# os module helps you to interact directly with the OS(operating system), you can perform operations directly from here.

# All of the example above are of in-built module.

# Importing my own module, that i have created in a new file-mymodule.py.

import mymodule
mymodule.hello()

import mymodule
mymodule.greet("Mohit", 1.778)

# Example of external module : to use an external module first you have to install that package in your python and to install the package, we use pip which is package manager for python.

# Requests : 

import requests
response = requests.get("https://www.google.com")   # .get is a function in requests that helps you to fetch the html code of an online page, here were trying to get the html page of google.com
print(response.text)   # .text which will show the html in text format.
print(response.status_code)   # .statuscode is a 3 digit number issued by server to client, through this you can check the status, ex: my output its 200 means it OK, the request was successful and the data was returned.