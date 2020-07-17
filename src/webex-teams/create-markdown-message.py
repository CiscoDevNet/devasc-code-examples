# Fill in this file with the messages code from the Webex Teams exercise

import requests

access_token = ''  # Make sure to add your access token here
room_id = '' # Add the roomId here
message = 'Hello **Devvie**' # This is your Markdown message
url = 'https://api.ciscospark.com/v1/messages'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params = {'roomId': room_id, 'markdown': message}
res = requests.post(url, headers=headers, json=params)
print(res.json())
