# Fill in this file with the code from the dna-center authenticate exercise

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import json
import sys

##### Cisco DNA Center URL and Authentication Credentials
# In a 'real' application, this information might be in a 'config.py' file
# to keep authentication and target information out of the primary logic

# - Authentication to DevAsc DNA Center
dnacip = "FILLINHOSTURL"
username = "FILLINUSER"
password = "FILLINPASSWORDHERE"
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

    # Supress credential warning for this exercise
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

    # Authentication API full URI
    post_uri = "https://"+dnacip+"/dna/system/api/v1/auth/token"
    print ("\nAuthenticate: POST %s"%(post_uri))

    try:
        # verify - set to False to tell requests to NOT verify server's TLS certificate
        #  In production code this should be left to default to 'True'
        r = requests.post(post_uri, auth=(username, password), verify=False)
        return r.json()["Token"]
    except:
        # Something wrong, cannot get access token
        print ("Status: %s"%r.status_code)
        print ("Response: %s"%r.text)
        sys.exit ()

# Authenticate to the Cisco DNA Center
# and obtain an authentication token
token = get_X_auth_token(dnacip, username, password)
print ("returned Authentication Token: ", (token))
