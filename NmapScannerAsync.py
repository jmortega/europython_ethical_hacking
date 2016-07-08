#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import optparse, nmap
import json
import argparse


def callbackMySql(host, result):
        try:
                script = result['scan'][host]['tcp'][3306]['script']
                
                print "Command line"+ result['nmap']['command_line']

                for key, value in script.items():
                        print 'Script {0} --> {1}'.format(key, value)
        except KeyError:
                # Key is not present
                pass

def callbackFTP(host, result):
        try:
                script = result['scan'][host]['tcp'][21]['script']
                
                print "Command line"+ result['nmap']['command_line']

                for key, value in script.items():
                        print 'Script {0} --> {1}'.format(key, value)
        except KeyError:
                # Key is not present
                pass
        
def callbackVNC(host, result):
        try:
                script = result['scan'][host]['tcp'][5900]['script']
                
                print "Command line"+ result['nmap']['command_line']

                for key, value in script.items():
                        print 'Script {0} --> {1}'.format(key, value)
        except KeyError:
                # Key is not present
                pass
        
def callbackPostgres(host, result):
        try:
                script = result['scan'][host]['tcp'][5432]['script']
                
                print "Command line"+ result['nmap']['command_line']

                for key, value in script.items():
                        print 'Script {0} --> {1}'.format(key, value)
        except KeyError:
                # Key is not present
                pass
        
def callbackMongoDB(host, result):
        try:
                script = result['scan'][host]['tcp'][27017]['script']
                
                print "Command line"+ result['nmap']['command_line']

                for key, value in script.items():
                        print 'Script {0} --> {1}'.format(key, value)
        except KeyError:
                # Key is not present
                pass
        
def callbackCassandra(host, result):
        try:
                script = result['scan'][host]['tcp'][9160]['script']
                
                print "Command line"+ result['nmap']['command_line']

                for key, value in script.items():
                        print 'Script {0} --> {1}'.format(key, value)
        except KeyError:
                # Key is not present
                pass
        
def callbackMySql(host, result):
        try:
                script = result['scan'][host]['tcp'][3306]['script']
                
                print "Command line"+ result['nmap']['command_line']

                for key, value in script.items():
                        print 'Script {0} --> {1}'.format(key, value)
        except KeyError:
                # Key is not present
                pass
        
def callbackSSL(host, result):
        try:
                script = result['scan'][host]['tcp'][443]['script']
                
                print "Command line"+ result['nmap']['command_line']

                for key, value in script.items():
                        print 'Script {0} --> {1}'.format(key, value)
        except KeyError:
                # Key is not present
                pass
        
def callbackSSH(host, result):
        try:
                script = result['scan'][host]['tcp'][22]['script']
                
                print "Command line"+ result['nmap']['command_line']

                for key, value in script.items():
                        print 'Script {0} --> {1}'.format(key, value)
        except KeyError:
                # Key is not present
                pass
        
def callbackHTTP(host, result):
        try:
                script = result['scan'][host]['tcp'][80]['script']
                
                print "Command line"+ result['nmap']['command_line']

                for key, value in script.items():
                        print 'Script {0} --> {1}'.format(key, value)
        except KeyError:
                # Key is not present
                pass
        

class NmapScannerAsync:
        
        def __init__(self):
                self.nmsync = nmap.PortScanner()
                self.nmasync = nmap.PortScannerAsync()
    
        def scanning(self):
                while self.nmasync.still_scanning():
                        self.nmasync.wait(5)    

        def nmapScan(self, hostname, port):
                try:
                        print "Checking port "+ port +" .........."
                        
                        self.nmsync.scan(hostname, port)
                
                        self.state = self.nmsync[hostname]['tcp'][int(port)]['state']
                        print " [+] "+ hostname + " tcp/" + port + " " + self.state                            

                        #mysql
                        if (port=='3306') and self.nmsync[hostname]['tcp'][int(port)]['state']=='open':
                                print 'Checking MYSQL port with nmap scripts......'
                                
                                #scripts for mysql:3306 open
                                print 'Checking mysql-audit.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p3306 --script mysql-audit.nse",callback=callbackMySql)
                                self.scanning()
                                print 'Checking mysql-brute.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p3306 --script mysql-brute.nse",callback=callbackMySql)
                                self.scanning()
                                print 'Checking mysql-databases.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p3306 --script mysql-databases.nse",callback=callbackMySql)
                                self.scanning()
                                print 'Checking mysql-databases.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p3306 --script mysql-dump-hashes.nse",callback=callbackMySql)
                                self.scanning()
                                print 'Checking mysql-dump-hashes.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p3306 --script mysql-empty-password.nse",callback=callbackMySql)
                                self.scanning()
                                print 'Checking mysql-enum.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p3306 --script mysql-enum.nse",callback=callbackMySql)
                                self.scanning()
                                print 'Checking mysql-info.nse".....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p3306 --script mysql-info.nse",callback=callbackMySql) 
                                self.scanning()
                                print 'Checking mysql-query.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p3306 --script mysql-query.nse",callback=callbackMySql)  
                                self.scanning()
                                print 'Checking mysql-users.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p3306 --script mysql-users.nse",callback=callbackMySql)  
                                self.scanning()
                                print 'Checking mysql-variables.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p3306 --script mysql-variables.nse",callback=callbackMySql) 
                                self.scanning()
                                print 'Checking mysql-vuln-cve2012-2122.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p3306 --script mysql-vuln-cve2012-2122.nse",callback=callbackMySql) 
                                self.scanning()
                                
                        #FTP
                        if (port=='21') and self.nmsync[hostname]['tcp'][int(port)]['state']=='open':
                                print 'Checking ftp port with nmap scripts......'
                                #scripts for ftp:21 open
                                print 'Checking ftp-anon.nse .....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p21 --script ftp-anon.nse",callback=callbackFTP)
                                self.scanning()
                                print 'Checking ftp-bounce.nse  .....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p21 --script ftp-bounce.nse",callback=callbackFTP)
                                self.scanning()
                                print 'Checking ftp-brute.nse  .....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p21 --script ftp-brute.nse",callback=callbackFTP)
                                self.scanning()
                                print 'Checking ftp-libopie.nse  .....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p21 --script ftp-libopie.nse",callback=callbackFTP)
                                self.scanning()
                                print 'Checking ftp-proftpd-backdoor.nse  .....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p21 --script ftp-proftpd-backdoor.nse",callback=callbackFTP)
                                self.scanning()
                                print 'Checking ftp-vsftpd-backdoor.nse   .....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p21 --script ftp-vsftpd-backdoor.nse",callback=callbackFTP)
                                self.scanning()
                
                        #vnc
                        if (port=='5900') and self.nmsync[hostname]['tcp'][int(port)]['state']=='open':
                                print 'Checking VNC port with nmap scripts......'
                                #scripts for vnc:5900 open
                                print 'Checking vnc-brute.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p5900 --script vnc-brute.nse",callback=callbackVNC)
                                self.scanning()
                                print 'Checking vnc-info.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p5900 --script vnc-info.nse",callback=callbackVNC)
                                self.scanning()
                                
                        #postgres
                        if (port=='5432') and self.nmsync[hostname]['tcp'][int(port)]['state']=='open':
                                print 'Checking POSTGRES port with nmap scripts......'
                                #scripts for postgres:5432 open
                                print 'Checking pgsql-brute.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p5432 --script pgsql-brute.nse",callback=callbackPostgres)
                                self.scanning()
                                
                        #mongodb
                        if (port=='27017') and self.nmsync[hostname]['tcp'][int(port)]['state']=='open':
                                print 'Checking MONGODB port with nmap scripts......'
                                #scripts for mondogb:27017 open
                                print 'Checking mongodb-brute.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p27017 --script mongodb-brute.nse",callback=callbackMongoDB)
                                self.scanning()
                                print 'Checking mongodb-databases.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p27017 --script mongodb-databases.nse",callback=callbackMongoDB)
                                self.scanning()
                                print 'Checking mongodb-info.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p27017 --script mongodb-info.nse",callback=callbackMongoDB)
                                self.scanning()
                                
                        #cassandra
                        if (port=='9160') and self.nmsync[hostname]['tcp'][int(port)]['state']=='open':
                                print 'Checking CASSANDRA port with nmap scripts......'
                                #scripts for cassandra:9160 open
                                print 'Checking cassandra-brute.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p9160 --script cassandra-brute.nse",callback=callbackCassandra)
                                self.scanning()
                                print 'Checking cassandra-info.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p9160 --script cassandra-info.nse",callback=callbackCassandra)
                                self.scanning()
                                
                        #ssl
                        if (port=='443') and self.nmsync[hostname]['tcp'][int(port)]['state']=='open':
                                print 'Checking SSL port with nmap scripts......'
                                #scripts for ssl:443 open
                                print 'Checking ssl-cert.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p443 --script ssl-cert.nse",callback=callbackSSL)
                                self.scanning()
                                print 'Checking ssl-date.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p443 --script ssl-date.nse",callback=callbackSSL)
                                self.scanning()
                                print 'Checking ssl-enum-ciphers.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p443 --script ssl-enum-ciphers.nse",callback=callbackSSL)
                                self.scanning()
                                print 'Checking ssl-google-cert-catalog.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p443 --script ssl-google-cert-catalog.nse",callback=callbackSSL)
                                self.scanning()
                                print 'Checking ssl-known-key.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p443 --script ssl-known-key.nse",callback=callbackSSL)
                                self.scanning()
                                print 'Checking sslv2.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p443 --script sslv2.nse",callback=callbackSSL)
                                self.scanning()
                                
                        #ssh
                        if (port=='22') and self.nmsync[hostname]['tcp'][int(port)]['state']=='open':
                                print 'Checking SSH port with nmap scripts......'
                                #scripts for SSH:22 open
                                print 'Checking ssh-hostkey.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p22 --script ssh-hostkey.nse",callback=callbackSSH)
                                self.scanning()
                                print 'Checking ssh2-enum-algos.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p22 --script ssh2-enum-algos.nse",callback=callbackSSH)
                                self.scanning()
                                print 'Checking sshv1.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p22 --script sshv1.nse",callback=callbackSSH)
                                self.scanning()
                                
                        #http
                        if (port=='80' or port=='8080') and self.nmsync[hostname]['tcp'][int(port)]['state']=='open':
                                print 'Checking HTTP port with nmap scripts......'
                                #scripts for http:80 open
                                print 'Obtain Hosts on IP hostmap-bfk.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p80 --script hostmap-bfk.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking dns-brute.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p80 --script dns-brute.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-adobe-coldfusion-apsa1301.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p80 --script http-adobe-coldfusion-apsa1301.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-affiliate-id.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p80 --script http-affiliate-id.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-apache-negotiation.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sS -p80 --script http-apache-negotiation.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-auth-finder.nse....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p80 --script http-auth-finder.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-auth.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p80 --script http-auth.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-awstatstotals-exec.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p80 --script http-awstatstotals-exec.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-axis2-dir-traversal.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p80 --script http-axis2-dir-traversal.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-backup-finder.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p80 --script http-backup-finder.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-barracuda-dir-traversal.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p80 --script http-barracuda-dir-traversal.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-barracuda-dir-traversal.nse....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p80 --script http-brute.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-cakephp-version.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p80 --script http-cakephp-version.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-chrono.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p80 --script http-chrono.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-coldfusion-subzero.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p80 --script http-coldfusion-subzero.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-comments-displayer.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p80 --script http-comments-displayer.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-config-backup.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p80 --script http-config-backup.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-cors.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p80 --script http-cors.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-date.nse....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p80 --script http-date.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-default-accounts.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p80 --script http-default-accounts.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-domino-enum-passwords.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p80 --script http-domino-enum-passwords.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-drupal-enum-users.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p80 --script http-drupal-enum-users.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-drupal-modules.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p80 --script http-drupal-modules.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-email-harvest.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p80 --script http-email-harvest.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-enum.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p80 --script http-enum.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-exif-spider.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p80 --script http-exif-spider.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-favicon.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p80 --script http-favicon.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-fileupload-exploiter.nse.....'
                                self.nmasync.scan(hosname,arguments="-A -sV -p80 --script http-fileupload-exploiter.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-form-brute.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p80 --script http-form-brute.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-form-fuzzer.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p80 --script http-form-fuzzer.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-frontpage-login.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p80 --script http-frontpage-login.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-generator.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p80 --script http-generator.nse",callback=callbackHTTP)
                                self.scanning()
                                self.nmasync.scan(hostname,arguments="-A -sV -p80 --script http-git.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-gitweb-projects-enum.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p80 --script http-gitweb-projects-enum.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-google-malware.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p80 --script http-google-malware.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-grep.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p80 --script http-grep.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-headers.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p80 --script http-headers.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-huawei-hg5xx-vuln.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p80 --script http-huawei-hg5xx-vuln.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-icloud-findmyiphone.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p80 --script http-icloud-findmyiphone.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-icloud-sendmsg.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p80 --script http-icloud-sendmsg.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-iis-webdav-vuln.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p80 --script http-iis-webdav-vuln.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-joomla-brute.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p80 --script http-joomla-brute.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-litespeed-sourcecode-download.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p80 --script http-litespeed-sourcecode-download.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-majordomo2-dir-traversal.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p80 --script http-majordomo2-dir-traversal.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-malware-host.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p80 --script http-malware-host.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-method-tamper.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p80 --script http-method-tamper.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-methods.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p80 --script http-methods.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-open-proxy.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p80 --script http-open-proxy.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-open-redirect.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p80 --script http-open-redirect.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-passwd.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p80 --script http-passwd.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-php-version.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p80 --script http-php-version.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-phpmyadmin-dir-traversal.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p80 --script http-phpmyadmin-dir-traversal.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking netbus-brute.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p80 --script http-phpself-xss.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-proxy-brute.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p80 --script http-proxy-brute.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-put.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p80 --script http-put.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-qnap-nas-info.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p80 --script http-qnap-nas-info.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-rfi-spider.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p80 --script http-rfi-spider.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-robots.txt.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p80 --script http-robots.txt.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-robtex-reverse-ip.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p80 --script http-robtex-reverse-ip.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-robtex-shared-ns.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p80 --script http-robtex-shared-ns.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-sitemap-generator.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p80 --script http-sitemap-generator.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-slowloris-check.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p80 --script http-slowloris-check.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-slowloris.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p80 --script http-slowloris.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-sql-injection.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p80 --script http-sql-injection.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking hhttp-stored-xss.nse....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p80 --script hhttp-stored-xss.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-title.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p80 --script http-title.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-tplink-dir-traversal.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p80 --script http-tplink-dir-traversal.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-trace.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p80 --script http-trace.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-traceroute.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p80 --script http-traceroute.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-unsafe-output-escaping.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p80 --script http-unsafe-output-escaping.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-userdir-enum.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p80 --script http-userdir-enum.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-vhosts.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p80 --script http-vhosts.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-virustotal.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p80 --script http-virustotal.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-vlcstreamer-ls.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p80 --script http-vlcstreamer-ls.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-vmware-path-vuln.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p80 --script http-vmware-path-vuln.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-vuln-cve2009-3960.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p80 --script http-vuln-cve2009-3960.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-vuln-cve2010-0738.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p80 --script http-vuln-cve2010-0738.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-vuln-cve2010-2861.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p80 --script http-vuln-cve2010-2861.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-vuln-cve2011-3192.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p80 --script http-vuln-cve2011-3192.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-vuln-cve2011-3368.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p80 --script http-vuln-cve2011-3368.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-vuln-cve2012-1823.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p80 --script http-vuln-cve2012-1823.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-vuln-cve2013-0156.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p80 --script http-vuln-cve2013-0156.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-waf-detect.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p80 --script http-waf-detect.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-waf-fingerprint.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p80 --script http-waf-fingerprint.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-wordpress-brute.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p80 --script http-wordpress-brute.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-wordpress-enum.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p80 --script http-wordpress-enum.nse",callback=callbackHTTP)
                                self.scanning()
                                print 'Checking http-wordpress-plugins.nse.....'
                                self.nmasync.scan(hostname,arguments="-A -sV -p80 --script http-wordpress-plugins.nse",callback=callbackHTTP)
                                self.scanning()                        
           
         
            
                except Exception,e:
                        print str(e)
                        print "Error to connect with " + hostname + " for port scanning" 
                        pass
        
    
    
    
if __name__ == "__main__":
        parser = argparse.ArgumentParser(description='Nmap scanner async')
            
        # Main arguments
        parser.add_argument("-target", dest="target", help="target IP / domain", required=True)
        parser.add_argument("-ports", dest="ports", help="Please, specify the target port(s) separated by comma[80,8080 by default]", default="80,8080")
    
        parsed_args = parser.parse_args()   

        port_list = parsed_args.ports.split(',')
    
        ip = parsed_args.target
    
        for port in port_list: 
                NmapScannerAsync().nmapScan(ip, port)
        
