# Add code for the Meraki hands-on lab here

import requests
import json

meraki_api_key = "8f90ecec4fca692f606092279f203c6020ca011c"
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
        url = "https://api.meraki.com/api/v0/networks/"+network['id']+"/devices"
        devices = requests.get(url,headers=headers)
        devices = devices.json()
        print(json.dumps(devices, indent=4))
        for device in devices:
            print(device['serial'])
