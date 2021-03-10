import requests

response = requests.get(url="http://localhost:5050/animals")
print(response.status_code)
print(response.json())
print(response.headers)

response = requests.get(url="http://localhost:5022/animals")
print(response.status_code)
print(response.json())
print(response.headers)

