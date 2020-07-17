# Fill in this file with the code from parsing YAML exercise

import json
import yaml

yaml_file = open("myfile.yaml","r")

pythondata = yaml.safe_load(yaml_file)

print(pythondata['expires_in'])

print("The access token from YAML is: %s" % pythondata['access_token'])
