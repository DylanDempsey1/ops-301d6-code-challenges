#!/usr/bin/env python3

# Challenge 06
# Dylan Dempsey
# 03/22/23
# Create a Python script that generates all directories, sub-directories and files for a user-provided directory path.




# Main

# import os module
import os

# Define a function that takes the user-provided directory path as an argument.
def generate_directory_structure(user_path):
   # Use os.walk() inside the function to iterate through the directories, sub-directories, and files. rint the directory, sub-directories, and files in a structured format.
    for root, dirs, files in os.walk(user_path):
        print(f"Directory: {root}")
        print("Sub-directories:"
        for directory in dirs:
            print(f"  - {directory}")
        print("Files:")
        for file in files:
            print(f"  - {file}")
        print("\n")

if __name__ == "__main__":
    user_path = input("Please enter a directory path: ")
    if os.path.exists(user_path) and os.path.isdir(user_path):
        generate_directory_structure(user_path)
    else:
        print("Invalid directory path. Please try again.")
              
# End 
      
# ChatGPT was referenced for this code.
