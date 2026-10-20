# shutil module, its very similar to os module but the difference is that its a bit powerful.


import shutil


shutil.move("John_doe.txt", "dir/")   # It will move the file John_doe.txt to 'dir' folder. It can also move a directory.


shutil.rmtree("dir")   # It will delete the directory, and it doesn't care if it is empty or not.

# Note: rmtree deletes the folder permanently with no recycle bin.


shutil.copy("John_doe.txt", "John_doe_copy.txt")   # It will copy the contents from John_doe.txt to John_doe_copy.txt, src (source) to dst (destination).

# Note: .copy, copies just the file content and the permission, if you also want timestamps preserved, use shutil.copy2.