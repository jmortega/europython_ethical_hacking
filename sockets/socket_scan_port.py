# Port Scanner
from socket import *                          # Imports socket module
ip=raw_input("Enter IP to scan : ")           # Asks user to enter IP address
start=input("Enter starting port number : ")  # Asks user to enter starting port number
end=input("Enter ending port number : ")      # Asks user to enter ending port number
print "Scanning IP: " , ip
for port in range(start,end):                 # For loop from starting to ending port
    print "Testing port "+str(port)+"...."
    s=socket(AF_INET, SOCK_STREAM)            # Creates a socket s
    s.settimeout(5) 	                      # set timeout  
    if(s.connect_ex((ip,port))==0):           # If connection to port was successful,then returns 0
        print "Port " , port, "is open"       # Prints open port
    s.close()                                 # Closes socket s
print "Scanning completed !! "
