# Fill in this file with the pagination code from the Webex Teams exercise

import requests
import json

access_token = '' # Make sure to add your access token here!
url = 'https://api.ciscospark.com/v1/memberships'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params = {
    "max": 1
}
res = requests.get(url, headers=headers, params=params)
formatted_message = """
Webex Teams API Response
----------------------------------
Response Status Code   : {}
Response Link Header   : {}
Response Body          : {}
-----------------------------------
""".format(res.status_code,  res.headers.get('Link'), json.dumps(res.json(), indent=4))
print(formatted_message)
