import requests

url = 'http://localhost:5000/messages'
data = {'email': 'navastest@gmail.com', 'content': 'Hello, World!'}
response = requests.post(url, json=data)
print(response.json())
