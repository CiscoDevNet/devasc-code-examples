# Add code for the Meraki hands-on lab here

import requests
import json

meraki_api_key = "8f90ecec4fca692f606092279f203c6020ca011c"
url =  "https://api.meraki.com/api/v0/organizations/566327653141842188/devices"
headers = {
        "X-Cisco-Meraki-API-Key": meraki_api_key,
    }
params = {
    "perPage": 3
}
res = requests.get(url, headers=headers, params=params)

# the next API request
second_response = requests.get(res.links['next']['url'], headers=headers)
formatted_message = """
Meraki Dashboard API Response
----------------------------------
Response Status Code   : {}
Response Link Header   : {}
Response Body          : {}
-----------------------------------
""".format(second_response.status_code,  second_response.headers.get('Link'), json.dumps(second_response.json(), indent=4))
print(formatted_message)
