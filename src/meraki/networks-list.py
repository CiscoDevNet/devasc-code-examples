# Add code for the Meraki hands-on lab here

import requests
import json

meraki_api_key = "8f90ecec4fca692f606092279f203c6020ca011c"
url =  "https://api.meraki.com/api/v0/organizations/566327653141842188/networks"
headers = {
        "X-Cisco-Meraki-API-Key": meraki_api_key,
    }
networks = requests.get(url,headers=headers)
print(json.dumps(networks.json(), indent=4))
