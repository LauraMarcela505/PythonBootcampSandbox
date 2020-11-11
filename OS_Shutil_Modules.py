# File paths need to be separated by \\

# write to a file
f = open("pracitce.txt","w+")
f.write("This is a test string")
f.close()


import os # works on any os

# current working directory
print(os.getcwd())

#arguement is the path
print(os.listdir()) # all files in a directory - list items
print(os.listdir("C:\\Users")) # can break down any part of a directory to see what files are there

import shutil # move files to different location

# moves to this location
# shutil.move('pracitce.txt',"C:\\Users\\laura") # source, destination parameters

import send2trash

print(os.listdir())

# send2trash.send2trash("pracitce.txt") deletes a text file

