#Use these commands in Kali to install required software:
#  sudo apt install python3-pip
#  pip install python-nmap

#======================================

# Import nmap so we can use it for the scan
import nmap
# re means regular expressions to ensure that the input is correctly formatted.
import re

# Pattern of IPv4 addresses.
ip_add_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
port_range_pattern = re.compile("([0-9]+)-([0-9]+)")
# Initialising the port numbers, will be using the variables later on.
port_min = 0
port_max = 65535

# This port scanner uses the Python nmap module.
# You'll need to install the following to get it work on Linux:
# Step 1: sudo apt install python3-pip
# Step 2: pip install python-nmap


# Basic user interface header
print(r"""    _        _        _           _     _ 
   / \   ___| | _____| | __ _  __| | __| |
  / _ \ / __| |/ / _ \ |/ _` |/ _` |/ _` |
 / ___ \\__ \   <  __/ | (_| | (_| | (_| |
/_/   \_\___/_|\_\___|_|\__,_|\__,_|\__,_|
""")
print("        ▂▃▅▆█ PORT SCANNER █▆▅▃▂     ")
print("\n****************************************************************")
print("\n* Constructed on 30 January, 2025                              *")
print("\n* https://github.com/RaianKibriaRohan                          *")
print("\n* https://www.linkedin.com/in/raian-kibria-rohan-89997a323/    *")
print("\n****************************************************************")

open_ports = []
# Ask user to input the ip address they want to scan.
while True:
    ip_add_entered = input("\nPlease enter the ip address that you want to scan: ")
    if ip_add_pattern.search(ip_add_entered):
        print(f"{ip_add_entered} is a valid ip address")
        break

while True:
    # You can scan 0-65535 ports. This scanner is basic and doesn't use multithreading so scanning 
    # all the ports is not advised.
    print("Please enter the range of ports you want to scan in format: <int>-<int> (ex would be 60-120)")
    port_range = input("Enter port range: ")
    port_range_valid = port_range_pattern.search(port_range.replace(" ",""))
    if port_range_valid:
        port_min = int(port_range_valid.group(1))
        port_max = int(port_range_valid.group(2))
        break

nm = nmap.PortScanner()
# We're looping over all of the ports in the specified range.
for port in range(port_min, port_max + 1):
    try:
        result = nm.scan(ip_add_entered, str(port))
        port_status = (result['scan'][ip_add_entered]['tcp'][port]['state'])
        print(f"Port {port} is {port_status}")
    except:
        # We cannot scan some ports and this ensures the program doesn't crash when we try to scan them.
        print(f"Cannot scan port {port}.")
        
