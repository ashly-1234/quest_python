
# importing shutil module 
import shutil 
import os
print(os.getcwd())
os.mkdir("A")
file = open("A/blank.txt", "x")
file.close()
os.mkdir("B")



 
source = "A/blank.txt"
destination ="B/blank.txt"
 
# Copy the content of 
# source to destination 
dest = shutil.copy("A/blank.txt", "B/blank.txt") 
 
# Print path of newly 
# created file 
print("Destination path:", "B/blank.txt")