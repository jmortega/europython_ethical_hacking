import socket
host = "192.168.56.101"
port = 21
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
	
	s.connect((host,port))
	#s.settimeout(5)
	data, addr = s.recvfrom(1024)
	print "recevied from ",addr
	print "obtained ", data
	s.close()
	
except socket.timeout,e :
	print e
	print "Client not connected"
	s.close()