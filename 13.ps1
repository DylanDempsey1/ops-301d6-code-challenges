#!/usr/bin/env powershell

# Ops 301 Code Challenge 13
# Dylan Dempsey
# 03/29/23
# Write a Powershell script that adds the below person to AD.

# Define variables
$FirstName = "Franz"
$LastName = "Ferdinand"
$Title = "TPS Reporting Lead"
$Company = "GlobeX USA"
$City = "Springfield"
$State = "OR"
$Department = "TPS Department"
$Email = "ferdi@GlobeXpower.com"
$Username = "fferdinand"

# Create the user
$ouPath = "OU=YourOU,DC=YourDomain,DC=com" # Replace with your organization's OU and domain
$Password = ConvertTo-SecureString "TemporaryPassword123" -AsPlainText -Force

New-ADUser -Name "$FirstName $LastName" `
    -GivenName $FirstName `
    -Surname $LastName `
    -Title $Title `
   
# End 

# ChatGPT was referenced for this code.
