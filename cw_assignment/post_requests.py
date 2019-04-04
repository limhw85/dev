import requests

data = {'title':'Python Requests','body':'Requests are awesome','userId':1} 
response = requests.post('https://jsonplaceholder.typicode.com/posts', data) 
print(response.status_code) 
print(response.text) 
