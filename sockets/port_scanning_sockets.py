import socket
rmip ='localhost'
portlist = [8080,22,23,80,912,135,445,20]
for port in portlist:
 sock= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
 result = sock.connect_ex((rmip,port))
 if result == 0:
  print port,": open"
 else:
  print port,": closed"
 sock.close()
