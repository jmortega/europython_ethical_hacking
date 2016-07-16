#!/usr/bin/env python

import sys
try:
    import nmap
except:
    sys.exit("[!] Install the nmap library: pip install python-nmap")

# Argument Validator
if len(sys.argv) != 3:
    sys.exit("Please provide two arguments the first being the targets the second the ports")

ports = str(sys.argv[2])
addrs = str(sys.argv[1])
portlist=ports.split(',')
print portlist

scanner = nmap.PortScanner()
scanner.scan(addrs, ports)
print scanner.all_hosts()

for host in scanner.all_hosts():
    print scanner[host]
    for port in portlist:
        state=scanner[host]['tcp'][int(port)]['state']
        print " [*] " + host + " tcp/"+port +" "+state    

