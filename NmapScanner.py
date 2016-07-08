#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import optparse, nmap
import json
import argparse


class NmapScanner:
     
    def __init__(self):
        self.nmsc = nmap.PortScanner()
    
    def nmapScan(self, host, port):
        try:
            print "Checking port "+ port +" .........."
            self.nmsc.scan(host, port)
            
            # Command info
            print "[*] Execuing command: %s" % self.nmsc.command_line()     
            self.state = self.nmsc[host]['tcp'][int(port)]['state']
            print " [+] "+ host + " tcp/" + port + " " + self.state
            
        except Exception,e:
            print "Error to connect with " + host + " for port scanning" 
            pass
        
    
    def nmapScanJSONGenerate(self, host, ports):
        try:
            print "Checking ports "+ str(ports) +" .........."
            self.nmsc.scan(host, ports)
            
            # Command info
            print "[*] Execuing command: %s" % self.nmsc.command_line()
            
            print self.nmsc.csv()
            results = {}     
            
            for x in self.nmsc.csv().split("\n")[1:-1]:
                splited_line = x.split(";")
                host = splited_line[0]
                proto = splited_line[1]
                port = splited_line[2]
                state = splited_line[4]
                
                try:
                    if state == "open":
                        results[host].append({proto: port})
                except KeyError:
                    results[host] = []
                    results[host].append({proto: port})
                
            # Store info
            file_info =  "scan_%s.json" % host
            with open(file_info, "w") as file_json:
                json.dump(results, file_json)
                
            print "[*] File '%s' was generated with scan results" % file_info            
    
        except Exception,e:
            print e
            print "Error to connect with " + host + " for port scanning" 
            pass
    


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Nmap scanner')
            
    # Main arguments
    parser.add_argument("-target", dest="target", help="target IP / domain", required=True)
    parser.add_argument("-ports", dest="ports", help="Please, specify the target port(s) separated by comma[80,8080 by default]", default="80,8080")
    
    parsed_args = parser.parse_args()   

    port_list = parsed_args.ports.split(',')
    
    ip = parsed_args.target
    
    for port in port_list: 
        NmapScanner().nmapScan(ip, port)
        
    NmapScanner().nmapScanJSONGenerate(ip,parsed_args.ports)
