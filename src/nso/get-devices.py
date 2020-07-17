# Add code from the NSO hands-on lab here

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

username = 'FILLINUSER'
password = 'FILLINPASSWORDHERE'

url = "https://FILLINHOSTURL/restconf/data/tailf-ncs:devices/device=ios0/config"

headers = {
    'Content-Type': "application/yang-data+json"
    }

# Supress credential warning for this exercise
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
response = requests.get(url,
                        auth=(username, password),
                        headers=headers,
                        verify=False)

print(response.text)
