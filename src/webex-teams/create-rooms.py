# Fill in this file with the code to create a new room from the Webex Teams exercise

import requests

access_token = ''  # Make sure to add your access token here
url = 'https://api.ciscospark.com/v1/rooms'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params={'title': 'DevNet Associate Training!'}
res = requests.post(url, headers=headers, json=params)
print(res.json())
