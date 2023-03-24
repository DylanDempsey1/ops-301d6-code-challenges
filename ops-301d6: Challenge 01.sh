#!/bin/bash

# Ops 3001d6 Code Challenge 01
# Dylan Dempsey
# 03/14/23
# Write a script that copies /var/log/syslog to current directory

# Main 

# Get the current date and time
current_date_time=$(date +"%Y%m%d-%H%M%S")

# Copy /var/log/syslog to the current working directory and append the current date and time to the filename
cp /var/log/syslog ./syslog_$current_date_time

# Executable Permission
chmod +x copy_syslog.sh

# Run Script
./copy_syslog.sh

# End


# ChatGPT was referenced for this code.