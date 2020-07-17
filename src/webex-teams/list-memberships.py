# Fill in this file with the membership code from the Webex Teams exercise

import requests

access_token = ''  # Make sure to add your access token here
room_id = ''
url = 'https://api.ciscospark.com/v1/memberships'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params = {'roomId': room_id}
res = requests.get(url, headers=headers, params=params)
print(res.json())
