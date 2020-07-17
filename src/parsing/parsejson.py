# Fill in this file with the code from parsing JSON exercise

import json
import yaml

with open('myfile.json','r') as json_file:
    ourjson = json.load(json_file)

json_file.close()
print(ourjson)

print(ourjson['expires_in'])

print("The access token from JSON is: %s" % ourjson['access_token'])
