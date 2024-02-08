import requests
endpoint = "http://localhost:8000/api/academic_list/" 

get_response = requests.get(endpoint) 

data = get_response.json()
print(data)