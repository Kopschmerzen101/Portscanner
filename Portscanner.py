import pyfiglet
import sys            # For handling system exit
import socket         # For creating network connections
from datetime import datetime  # For timestamping the scan start time

# Display ASCII banner for the port scanner
import pyfiglet       # For generating the ASCII art banner 
ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)

# Ask user to input the target IP address for scanning
target = input("Target IP: ")

# Display banner information about the target and start time of the scan
print("_" * 50)
print("Scanning Target: " + target)
print("Scanning started at: " + str(datetime.now()))
print("_" * 50)

try:
    # Loop through a range of ports to scan (from port 1 to 65534)
    for port in range(1, 65535):
        # Create a socket to connect to the target
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Set default timeout for connection attempts (0.5 seconds)
        socket.setdefaulttimeout(0.5)
        
        # Attempt to connect to the target IP on the specified port
        result = s.connect_ex((target, port))
        # If the result is 0, the port is open
        if result == 0:
            print("[*] Port {} is open".format(port))
            s.close()  # Close the socket after checking the port
            
except KeyboardInterrupt:
    # Handle Ctrl+C interruption gracefully and exit
    print("\n Exiting :(")
    sys.exit()
    
except socket.error:
    # Handle errors when the host is unreachable
    print("\n Host not responding :(")
    sys.exit()
