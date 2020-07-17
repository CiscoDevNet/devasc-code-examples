# Add code for the Meraki hands-on lab here

import requests
import json

meraki_api_key = "FILLINKEYHERE"
url =  "https://api.meraki.com/api/v0/organizations/566327653141842188/devices"
headers = {
        "X-Cisco-Meraki-API-Key": meraki_api_key,
    }
params = {
    "perPage": 3
}
res = requests.get(url, headers=headers, params=params)
formatted_message = """
Meraki Dashboard API Response
----------------------------------
Response Status Code   : {}
Response Link Header   : {}
Response Body          : {}
-----------------------------------
""".format(res.status_code,  res.headers.get('Link'), json.dumps(res.json(), indent=4))
print(formatted_message)
