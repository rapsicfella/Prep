# OS Operations
#Listing Files and Directories:

import os
import subprocess

directory = "/path/to/directory"
files = os.listdir(directory)

for file in files:
    print(file)
    
# Creating Directories:

new_directory = "/path/to/new_directory"
os.mkdir(new_directory)


# Executing Shell Commands:
# You can run shell commands and scripts from Python using the subprocess module.

command = "ls -l"
result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

if result.returncode == 0:
    print("Output:")
    print(result.stdout)
else:
    print("Error:")
    print(result.stderr)


# Renaming Files:



old_name = "/path/to/old_name.txt"
new_name = "/path/to/new_name.txt"
os.rename(old_name, new_name)