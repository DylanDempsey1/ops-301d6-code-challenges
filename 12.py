#/usr/bin/env python3

# Ops 301 Challenge 12
# Dylan Dempsey
# 03/28/23
# Create a python script that uses the requests library:
# - Prompts the user to type a string as destiantion url
# - Prompts user to select a HTTP method:
#   - GET
#   - POST
#   - PUT
#   - DELETE
#   - HEAD
#   - PATCH
#   - OPTIONS
# Print to the screen the entire request the script is about to send. Ask the user to confirm the request.
# For the given header translate the error code into a human readable error message.
# For the fiven URL print the response header to the screen

# Main

# Prompt the user to input the destination URL
url = input("Enter the destination URL: ")

# Prompt the user to select an HTTP method
http_methods = ["GET", "POST", "PUT", "DELETE", "HEAD", "PATCH", "OPTIONS"]
print("Select an HTTP method from the following options:")
for index, method in enumerate(http_methods):
    print(f"{index + 1}. {method}")

method_choice = int(input("Enter the number corresponding to your choice: ")) - 1
selected_method = http_methods[method_choice]

# Print the request details and ask for confirmation
print(f"\nYour request details:")
print(f"URL: {url}")
print(f"HTTP Method: {selected_method}")
confirmation = input("\nProceed with the request? (yes/no): ")

if confirmation.lower() == "yes":
    # Perform the chosen HTTP request
    response = requests.request(selected_method, url)

    # Translate the status code into plain terms
    status_code = response.status_code
    if status_code == 200:
        status_message = "OK"
    elif status_code == 404:
        status_message = "Site not found"
    else:
        status_message = f"Status code: {status_code}"

    # Print the translated status code and response header information
    print(f"\nResponse status: {status_message}")
    print("Response headers:")
    for key, value in response.headers.items():
        print(f"{key}: {value}")
else:
    print("Request canceled.")

# End 

#ChatGPT was referenced for this code