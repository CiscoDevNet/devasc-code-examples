# Fill in this file with the people listing code from the Webex Teams exercise

import requests

access_token = ''  # Make sure to add your access token here
url = 'https://api.ciscospark.com/v1/people'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params = {
    'email': '' # Make sure you add your users's email address here
}
res = requests.get(url, headers=headers, params=params)
print(res.json())

person_id = '' # Add your ID here, which you get from the prior request
url = 'https://api.ciscospark.com/v1/people/{}'.format(person_id)
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
res = requests.get(url, headers=headers)
print(res.json())
