'''
3. OS and Shutil Modules

1 - Use the os module to:
Print the current working directory
List all files and folders in the current directory
Create a new folder my_folder
'''

import os

print(os.getcwd())

print(os.listdir("."))

os.mkdir("my_folder")   # Note: it will crash if you run it twice. cause the folder already exists, showing error: FileExistsError.

'''
# Other ways to make directory

if not os.path.exists("my_folder"):
    os.mkdir("my_folder")


try:
    os.mkdir("my_folder")
except FileExistsError:
    print("Folder already exists")
'''