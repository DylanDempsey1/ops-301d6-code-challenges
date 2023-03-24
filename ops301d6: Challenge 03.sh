#!bin/bash/

# Ops 301d6 Code Challenge 03
# Dylan Dempsey
# 03/16/23
# Create a bash script that launches a menu system with the following options:

# Main

while true; do
echo Menu:
echo "1. Hello world!"
echo "2. Ping self"
echo "3. IP info"
echo "4. Exit"
echo -n "Please select your choice: "
read choice 

case $choice in
1)
    echo "Hello world!"
    ;;
2)
    ping -c 192.168.0.40
    ;;
3)
     if [ $(uname) == "Darwin" ]; then
                ifconfig
            else
                ip addr
            fi
            ;;
        4)
            echo "Exiting..."
            exit 0
            ;;
        *)
            echo "Invalid choice. Please try again."
            ;;
    esac
    echo
done

# End

# ChatGPT was referenced for this code