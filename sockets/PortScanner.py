import argparse
from socket import *

# Usage: #python  PortScanner.py -a 192.168.0.1 -p 21,80

def printBanner(connSock,tgtPort):
    try:
        # Send data to target
        if(tgtPort == 80):
            connSock.send("GET HTTP/1.1 \r\n")
        else:
            connSock.send("\r\n")
            
        # Receive data from target
        results = connSock.recv(4096)
        # print the banner
        print '[+] Banner:' + str(results)
    except:
        print '[-] Banner not available\n'

def connScan(tgtHost,tgtPort):
    try:
        # Create the socket object
        connSock=socket(AF_INET,SOCK_STREAM)
        # try to connect with the target
        connSock.connect((tgtHost,tgtPort))
        print '[+] %d tcp open'% tgtPort
        printBanner(connSock,tgtPort)
    except:
        # Print the failure results
        print '[+] %d tcp closed'% tgtPort
    finally:
        # close the socket object
        connSock.close()

def portScan(tgtHost,tgtPorts):
    try:
        #if -a was not an IP address this will resolve it to an IP/ if it's an IP that's fine it will return the same IP
        tgtIP = gethostbyname(tgtHost)
    except:
        print "[-] Error: Unknown Host"
        exit(0)

    try:
        # if the domain can be resolved that's good, the results will be something like: ('domain.com', [], ['20.13.64.15'])
        tgtName = gethostbyaddr(tgtIP)
        print "[+]--- Scan result for: " + tgtName[0] + " ---"
    except:
        print "[+]--- Scan result for: " + tgtIP + " ---"

    setdefaulttimeout(10)

    # For each port number call the connScan function
    for tgtPort in tgtPorts:
        connScan(tgtHost, int(tgtPort))

def main():
    # Parse the command line arguments
    parser = argparse.ArgumentParser('Smart TCP Client Scanner') 
    parser.add_argument("-a","--address", type=str, help="The target IP address")
    parser.add_argument("-p","--port", type=str, help="The port number to connect with")
    args = parser.parse_args()

    # Store the arguments values
    ipaddress = args.address
    portNumbers = args.port.split(',')
    
    #Call the Port Scan function
    portScan(ipaddress,portNumbers)
        
if __name__ == "__main__":
    # Call the main function
    main()
