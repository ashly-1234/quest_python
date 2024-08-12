'''
Write a program to move a file in directory 'source' and copy it to 'destination'. Handle necessary exceptions:
1. if file does not exists in source, print "no file found in source".

'''

import shutil
import os

# Creating directories and files
os.mkdir("A")
file = open("A/blank.txt", "x")
file.close()
os.mkdir("B")

source = "A/blank.txt"
destination = "B/blank.txt"

try:
    # Check if the file exists in the source
    file_found = os.path.exists(source)
    
    if not file_found:
        print("No file found in source")
    else:
        # Move the file from source to destination
        shutil.move(source, destination)
        print("File moved successfully")
        print("Destination path:", destination)

except Exception as e:
    print(f"An error occurred: {e}")
