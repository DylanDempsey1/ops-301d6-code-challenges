#!/usr/bin/env python3

# Ops Challenge 11
# Dylan Dempsey 
# 03/28/23
# Write a python script using Psutil

# Main

import psutil

# Fetch CPU times
cpu_times = psutil.cpu_times()

# Extract required information
user_time = cpu_times.user
system_time = cpu_times.system
idle_time = cpu_times.idle
nice_time = cpu_times.nice
io_wait_time = cpu_times.iowait
hardware_interrupt_time = cpu_times.irq
software_interrupt_time = cpu_times.softirq
steal_time = cpu_times.steal
guest_time = cpu_times.guest

# Print the information
print(f"Time spent by normal processes executing in user mode: {user_time} seconds")
print(f"Time spent by processes executing in kernel mode: {system_time} seconds")
print(f"Time when system was idle: {idle_time} seconds")
print(f"Time spent by priority processes executing in user mode: {nice_time} seconds")
print(f"Time spent waiting for I/O to complete: {io_wait_time} seconds")
print(f"Time spent for servicing hardware interrupts: {hardware_interrupt_time} seconds")
print(f"Time spent for servicing software interrupts: {software_interrupt_time} seconds")
print(f"Time spent by other operating systems running in a virtualized environment: {steal_time} seconds")
print(f"Time spent running a virtual CPU for guest operating systems under the control of the Linux kernel: {guest_time} seconds")

# End 


#ChatGPT was referenced for this code
