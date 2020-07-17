# Add code for the Meraki hands-on lab here

import requests
import json

meraki_api_key = "FILLINKEYHERE"
url =  "https://api.meraki.com/api/v0/networks/L_566327653141858543/devices"
headers = {
        "X-Cisco-Meraki-API-Key": meraki_api_key,
    }
devices = requests.get(url,headers=headers)
print(json.dumps(devices.json(), indent=4))
