'''
2 - Use the shutil module to:
Copy a file from one folder to another
Move a file to a new folder
Delete a file (careful: irreversible!)
'''

import shutil
import os

shutil.copy("copy.txt", "my_folder\\copy.txt")
shutil.move("move.txt", "my_folder")   # After the file has been moved once, if you run again it will show an error.
os.remove("copy.txt")   # shutil has no function to delete a file, so we have to use os module here.