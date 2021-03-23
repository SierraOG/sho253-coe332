import requests

response = requests.get(url="http://localhost:5022/animals")
print(response.status_code)
print(response.json())
print(response.headers)

response = requests.get(url="http://localhost:5022/animals/body/emu")
print(response.status_code)
print(response.json())
print(response.headers)

response = requests.get(url="http://localhost:5022/animals/tails/12")
print(response.status_code)
print(response.json())
print(response.headers)
