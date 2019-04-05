
import requests
import os

os.system("/home/hanwee/repo/cw_assignment/get_ansible_token.sh")


str = open('/home/hanwee/repo/cw_assignment/token.txt', 'r').read()
#print(str[14:44])


auth_token=(str[14:44])
hed = {'Authorization': 'Bearer ' + auth_token}
data = {'projects' : 'name'}

#url = 'https://ansible-server/api/v2/job_templates/'
url = 'https://ansible-server/api/v2/jobs/7/'
response = requests.get(url, json=data, headers=hed , verify=False)
print(response)
print(response.json())
