import requests

# Reset data
print("Reseting data")
response = requests.get(url="http://localhost:5025/animals/reset")

# Get all animals
print("Getting all animals")
response = requests.get(url="http://localhost:5025/animals")
print(response.status_code)
print(response.json())
print(response.headers)

# Endpoints from previous homework
# response = requests.get(url="http://localhost:5025/animals/body/toad")
# print(response.status_code)
# print(response.json())
# print(response.headers)

# response = requests.get(url="http://localhost:5025/animals/head/snake")
# print(response.status_code)
# print(response.json())
# print(response.headers)

# Get animal by id
print("Getting animal by id c7c48301-ec06-46b0-84fa-40bc0d37e90f")
response = requests.get(url="http://localhost:5025/animals/id/c7c48301-ec06-46b0-84fa-40bc0d37e90f")
print(response.status_code)
print(response.json())
print(response.headers)

# Update animal by id
print("Updating animal by id c7c48301-ec06-46b0-84fa-40bc0d37e90f")
response = requests.get(url="http://localhost:5025/animals/update/id/c7c48301-ec06-46b0-84fa-40bc0d37e90f/panda/emu-bee/3/6/12")

# Get animals by date range
print("Getting animals created between 29/03/2021-16:35:25 to 29/03/2021-16:35:28")
response = requests.get(url="http://localhost:5025/animals/date/29/03/2021-16:35:25/29/03/2021-16:35:28")
print(response.status_code)
print(response.json())
print(response.headers)

# Delete animals by date range
print("Deleting animals created between 29/03/2021-16:35:25 to 29/03/2021-16:35:28")
response = requests.get(url="http://localhost:5025/animals/delete/date/29/03/2021-16:35:25/29/03/2021-16:35:28")
print(response.status_code)
print(response.json())
print(response.headers)

# Get average legs
print("Getting average legs")
response = requests.get(url="http://localhost:5025/animals/average/legs")
print(response.status_code)
print(response.json())
print(response.headers)

# Get total animals
print("Getting total animals")
response = requests.get(url="http://localhost:5025/animals/total")
print(response.status_code)
print(response.json())
print(response.headers)
