# Add code for the Meraki hands-on lab here

import requests
import json

meraki_api_key = "FILLINKEYHERE"
url =  "https://api.meraki.com/api/v0/organizations"
headers = {
        "X-Cisco-Meraki-API-Key": meraki_api_key,
    }
orgs = requests.get(url,headers=headers)
orgs = orgs.json()
print(json.dumps(orgs, indent=4))

for org in orgs:
    print(org['id'])
    url = "https://api.meraki.com/api/v0/organizations/"+org['id']+"/networks"
    networks = requests.get(url,headers=headers)
    networks = networks.json()
    print(json.dumps(networks, indent=4))
    for network in networks:
        print(network['id'])

import requests
import json

meraki_api_key = "FILLINKEYHERE"
url =  "https://api.meraki.com/api/v0/organizations"
headers = {
        "X-Cisco-Meraki-API-Key": meraki_api_key,
    }
orgs = requests.get(url,headers=headers)
orgs = orgs.json()
print(json.dumps(orgs, indent=4))

for org in orgs:
    print(org['id'])
    url = "https://api.meraki.com/api/v0/organizations/"+org['id']+"/networks"
    networks = requests.get(url,headers=headers)
    networks = networks.json()
    print(json.dumps(networks, indent=4))
    for network in networks:
        print(network['id'])
