"""
os and shutil module, both are in-built and are used to manipulate files and directory.

To use them you can directly import them.
"""

import os


# To print the name of the current directory.

current_directory = os.getcwd()   # prints the name of the current directory.
print("Name of current directory:",current_directory)


# To list all the files and folder in a current directory.

files = os.listdir(".")   # List all the files and folder in a current directory. and "." represents current directory.
print("Files in current directory:", files)

files_sub = os.listdir("dir")  # It will list but of (dir) directory.
print("Files in sub-directory (dir):", files_sub)


# To know if a file/folder exists.

if os.path.exists("dir"):
    print("File/folder does exist.")

# Another way.
print(os.path.exists("john_doe.txt"))

# Note: it gives output in True / False.


'''
To change the current directory in which you are in
os.chdir("dir")
'''


'''
To create a new directory.
os.mkdir("new_directory")
'''


'''
To remove a file

os.remove("Credentials.txt")
'''


'''
# Removes only the empty directory.

os.rmdir("dir")
'''


'''
Will rename a file or directory

os.rename("credentials.txt", "password.txt")
'''


# Remember: all of these functions are used to work with files and directory in an operating system.