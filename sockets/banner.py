import socket
import http_proxy_connect

(s,status,response_headers) = http_proxy_connect.http_proxy_connect(('ep2016.europython.eu',80), ('10.129.8.100',8080))
s.send('GET / HTTP/1.1\r\nHost: ep2016.europython.eu\r\n\r\n')
data = s.recv(2048)
s.close()
print data
