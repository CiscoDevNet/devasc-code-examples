# Fill in this file with the code to get the next page of data from the Webex Teams exercise

# Make the next paginated API request
import requests
import json

access_token = ''  # Make sure to add your access token here
url = 'https://api.ciscospark.com/v1/memberships'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params = {
    "max": 1
}
res = requests.get(url, headers=headers, params=params)

second_response = requests.get(res.links['next']['url'], headers=headers)
formatted_message = """
Webex Teams Second API Response
----------------------------------
Response Status Code   : {}
Response Link Header   : {}
Response Body          : {}
-----------------------------------
""".format(second_response.status_code,  second_response.headers.get('Link'), json.dumps(second_response.json(), indent=4))
print(formatted_message)
