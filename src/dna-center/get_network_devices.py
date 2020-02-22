# Fill in this file with the code from the DNA Center Get Network Devices exercise

import requests
# requests documentation: https://requests.readthedocs.io/en/master/
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import json
import sys

##### Cisco DNA Center URL and Authentication Credentials
# In a 'real' application, this information might be in a 'config.py' file
# to keep authentication and target information out of the primary logic
# - Authentication to DevAsc DNA Center
dnacip = "devasc-dnacenter-1.cisco.com"
username = "devnetuser"
password = "C!3c0d$Y"
#####

# define Authentication method
def get_X_auth_token(dnacip,username,password):
    """
    Authenticate to remote Cisco DNA Center

    Parameters
    ----------
    dnacip (str): dnac routable DNS address or ip
    username (str): dnac user name
    password (str): password

    Return:
    ----------
    str: dnac access token
    """

    # Suppress credential warning for this exercise
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

    # Authentication API full URI
    post_uri = "https://"+dnacip+"/dna/system/api/v1/auth/token"
    print ("\nAuthenticate: POST %s"%(post_uri))

    try:
        # verify=False to suppress verify server's TLS certificate
        #  In production code this should be left to default to 'True'
        r = requests.post(post_uri, auth=(username, password), verify=False)
        return r.json()["Token"]
    except:
        # Failed to obtain access token
        print ("Status: %s"%r.status_code)
        print ("Response: %s"%r.text)
        sys.exit ()

# Get Network Device API wrapper
def get_network_device(dnacip, headers, params, modifier):
    """
    GET Network Device API wrapper
    This function returns the response from a Get Network Device request
    if Status = 200
    else it prints the Status and reponse and aborts.

    Parameters
    ----------
    dnacip (str): dnac routable DNS address or ip
    headers: headers for request
    params: parameters to be added to the GET request.

    Return:
    ----------
    response
    """

    # Get Network Device URI
    uri = "https://"+dnacip+"/dna/intent/api/v1/network-device"+modifier
    try:
        if params == "":
            print ("\n---\nGET %s"%(uri))
        else:
            print ("\n---\nGET %s?%s"%(uri,params))

        resp = requests.get(uri,headers=headers,params=params,verify = False)
        return resp
    except:
        # Something went wrong. Provide status informaton and terminate
        print ("Status: %s"%r.status_code)
        print ("Response: %s"%r.text)
        sys.exit ()

# Authenticate to the Cisco DNA Center
# and obtain an authentication token
token = get_X_auth_token(dnacip, username, password)
print ("returned Authentication Token: ", (token))

# assign the authentication token to a header key value pair
# 'x-auth-token'={{token}}
headers = {"x-auth-token": token}

# Start by getting a count of all devices of all types known to the Cisco DNA Center
# by appending "/count" to the Get Network_Devices URI
params=""
modifier="/count"
resp = get_network_device(dnacip, headers, params, modifier)
print ("All devices count: ",json.dumps(resp.json()["response"]))

# Focus on just those devices that are Cisco 9300 Switches.
# Use a filter to limit responses to '9300 Series Switches'

# Start with a count of those devices
params="series=Cisco Catalyst 9300 Series Switches"
modifier="/count"
resp = get_network_device(dnacip, headers, params, modifier)

switch_count = int(json.dumps(resp.json()["response"]))
print ("Catalyst 9300 Switch count: ",switch_count)

# Request a list of the Cisco 9300 Switches
# (remove the '/count' modifier, but leave the filter in place)
modifier = ""
resp = get_network_device(dnacip, headers, params, modifier)
print ("Catalyst 9300 Switch list: ",json.dumps(resp.json()["response"], indent=4))

# Focus in on key information from these devices and pull out just
# key identifying information such as device Type, Id, serial number, and IPv4

json_resp = resp.json()["response"]

for i in range(0, switch_count):
    print("Switch %d:  Type: %s.  Serial Number: %s.  DeviceId: %s. Mgmt IPv4: %s"
      %(i, json_resp[i]['type'], json_resp[i]['serialNumber'],json_resp[i]['id'],
        json_resp[i]['managementIpAddress']))

# Finally, use each device identifier to discover the VLANs associated to that switch
params = ""

for i in range(0, switch_count):
    modifier = "/"+json_resp[i]['id']+"/vlan"
    resp = get_network_device(dnacip, headers, params, modifier)
    print("Device Serial Number %s is attached to VLANs:"%(json_resp[i]['serialNumber']))
    print(json.dumps(resp.json()["response"],indent=4))
