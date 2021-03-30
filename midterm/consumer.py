import requests

# Reset data
print("Reseting data")
response = requests.get(url="http://localhost:5025/animals/reset")

# Get all animals
print("\nGetting all animals")
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
print("\nGetting animal by id c7c48301-ec06-46b0-84fa-40bc0d37e90f")
response = requests.get(url="http://localhost:5025/animals/id/c7c48301-ec06-46b0-84fa-40bc0d37e90f")
print(response.status_code)
print(response.json())
print(response.headers)

# Update animal by id
print("\nUpdating animal by id c7c48301-ec06-46b0-84fa-40bc0d37e90f")
response = requests.get(url="http://localhost:5025/animals/update/id/c7c48301-ec06-46b0-84fa-40bc0d37e90f/panda/emu-bee/3/6/12")

print("\nChecking updated animal has changed with id c7c48301-ec06-46b0-84fa-40bc0d37e90f")
response = requests.get(url="http://localhost:5025/animals/id/c7c48301-ec06-46b0-84fa-40bc0d37e90f")
print(response.status_code)
print(response.json())
print(response.headers)

# Get animals by date range
print("\nGetting animals created between 29-03-2021-16:35:25 to 29-03-2021-16:35:28")
response = requests.get(url="http://localhost:5025/animals/date/29-03-2021-16:35:25/29-03-2021-16:35:28")
print(response.status_code)
print(response.json())
print(response.headers)

# Delete animals by date range
print("\nDeleting animals created between 29-03-2021-16:35:25 to 29-03-2021-16:35:28")
response = requests.get(url="http://localhost:5025/animals/delete/date/29-03-2021-16:35:25/29-03-2021-16:35:28")

print("\nChecking animals were deleted between 29-03-2021-16:35:25 to 29-03-2021-16:35:28")
response = requests.get(url="http://localhost:5025/animals/date/29-03-2021-16:35:25/29-03-2021-16:35:28")
print(response.status_code)
print(response.json())
print(response.headers)

# Get average legs
print("\nGetting average legs")
response = requests.get(url="http://localhost:5025/animals/average/legs")
print(response.status_code)
print(response.json())
print(response.headers)

# Get total animals
print("\nGetting total animals")
response = requests.get(url="http://localhost:5025/animals/total")
print(response.status_code)
print(response.json())
print(response.headers)
