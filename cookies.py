import requests
import time

def check_httponly(c):
	if 'httponly' in c._rest.keys():
		return 'True'
	else:
		return 'False'

url='http://ep2016.europython.eu/en/'
req = requests.get(url)

print req.cookies
cookies = dict(admin='True')

cookie_req = requests.get(url, cookies=cookies)

for cookie in req.cookies:
	print 'Name:', cookie.name
	print 'Value:', cookie.value
	print 'Secure:', cookie.secure
	print 'Loosly defined domain:', cookie.domain_initial_dot
	print 'HTTPOnly:', check_httponly(cookie), '\n'
