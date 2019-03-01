#Need to install requests package for python
#easy_install requests
import sys
import requests

# Set the request parameters
url = 'https://dev66195.service-now.com/api/now/table/incident/5646e7f6dbb32300095258b3ca9619e8'

# Eg. User name="admin", Password="admin" for this code sample.
user = 'admin'
pwd = 'Mechanics@565'

# Set proper headers
headers = {"Content-Type":"application/json","Accept":"application/json"}

# Do the HTTP request
response = requests.get(url, auth=(user, pwd), headers=headers )

# Check for HTTP codes other than 200
if response.status_code != 200: 
    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
    exit()

# Decode the JSON response into a dictionary and use the data
data = response.json()
#sys.stdout = open('file', 'w')


print(data)



