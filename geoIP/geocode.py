import urllib
import json
import requests

# 1. Build the URL. 
form = { "address": "333 waterside drive, norfolk, va, 23510", "sensor": "false", "key": "AIzaSyB2KqDo8LDMrlzH9nmKN2XMHk-ZM2ib8-g" } 

query = urllib.urlencode(form)
print query
scheme_netloc_path = "https://maps.googleapis.com/maps/api/geocode/json"

print(scheme_netloc_path+"?"+query)

# 2. Send the request;get the response.

r = requests.get(scheme_netloc_path+"?"+query,verify=False)
json_data = r.json()
print json_data

#encoded
data_string = json.dumps(json_data)

print data_string

#Decoded
decoded = json.loads(data_string)

print decoded

for alt in decoded['results']:
 print(alt['types'], alt['formatted_address'])
 print(alt['address_components'])