# Add code for the Meraki hands-on lab here

import requests
import json

meraki_api_key = "FILLINKEYHERE"
url =  "https://api.meraki.com/api/v0/organizations"
headers = {
        "X-Cisco-Meraki-API-Key": meraki_api_key,
    }
orgs = requests.get(url,headers=headers)
print(json.dumps(orgs.json(), indent=4))
