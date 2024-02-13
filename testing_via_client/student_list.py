import requests

# Your token
token = "8a0f6d9469106159bd39d061cbc2127dcd36b4b9"

# URL of the API endpoint you want to access
url = "http://127.0.0.1:8000/api/academic/create/"

# Construct the headers with the Authorization token
headers = {
    "Authorization": f"Bearer {token}",
}

# Make the GET request with the headers
response = requests.get(url, headers=headers)

# Check the response
print(response.status_code)
print(response.json())  # or use response.text if it's not JSON
