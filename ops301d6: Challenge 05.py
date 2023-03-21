#!/usr/bin/env python3

# Ops 301d6 Code Challenge 05
# Dylan Dempsey
# 03/20/23
# Write a python script with bash commands!

# Import os
import os

# Use os.system to call bash command
var1 = (os.system("whoami"))
var2 = (os.system("ip a"))
var3 = (os.system("lshw -short"))

# Use the print command three times
print (var1)
print (var2)
print (var3)
