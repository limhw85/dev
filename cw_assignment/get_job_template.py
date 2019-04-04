
import requests
import os

os.system("/home/hanwee/get_ansible_token.sh")


str = open('/home/hanwee/token.txt', 'r').read()
print(str[14:44])


auth_token=(str[14:44])
hed = {'Authorization': 'Bearer ' + auth_token}
data = {'projects' : 'name'}

url = 'https://10.10.7.179/api/v2/job_templates/'
#response = requests.post(url, json=data, headers=hed , verify=False)
response = requests.get(url, json=data, headers=hed , verify=False)
print(response)
print(response.json())
