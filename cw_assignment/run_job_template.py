# import the request library
import requests
import os

#os.system("/home/hanwee/repo/cw_assignment/get_ansible_token.sh")
str = open('/home/hanwee/repo/cw_assignment/token.txt', 'r').read()

# API key here
api_key=(str[14:44])

# API endpoint
url = 'https://ansible-server/api/v2/job_templates/6/launch/'
#url = 'https://ansible-server/api/v2/jobs/7/relaunch/'
auth_token=(str[14:44])
hed = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + auth_token}


# data to be sent to api
#data = {'projects' : 'name'}
data = {
    "credentials": [
        1
    ],
    "credential_passwords": {
        "vault_password": "P@ssw0rd"
    }
}



#url = 'https://10.10.7.179/api/v2/job_templates/'
#response = requests.get(url, json=data, headers=hed,  verify=False)
#response = requests.get(url, headers=hed,  verify=False)
response = requests.post(url, headers=hed, verify=False)
print(response)
print(response.json())
