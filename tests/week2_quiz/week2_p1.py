'''
Write a program to move a file in directory 'source' and copy it to 'destination'. Handle necessary exceptions:
1. if file does not exists in source, print "no file found in source".
2. if same file already exists in target, print "file with same name already exists"

'''

import shutil 
import os
print(os.getcwd())
os.mkdir("A")
file = open("A/blank.txt", "x")
file.close()
os.mkdir("B")

 
source = "A/blank.txt"
destination ="B/blank.txt"

dest = shutil.copy("A/blank.txt", "B/blank.txt") 

print("Destination path:", "B/blank.txt")

file_found = True
if file_found is True:
    print("file found")
else:
    print("not found")
    