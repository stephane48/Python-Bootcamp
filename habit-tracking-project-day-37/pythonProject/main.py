import requests
from datetime import datetime

USERNAME = "sessegnon"
TOKEN = "fdfsddcvscvscvc"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

## Step to create user
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

add_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_params['id']}"

today = datetime.now()
# print(today.strftime("%Y%m%d"))

pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometers did you cycle today? "),
}

response = requests.post(url=add_pixel_endpoint, json=pixel_params, headers=headers)
print(response.text)

put_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_params['id']}/{pixel_params['date']}"

put_params = {
    "quantity": "7.75"
}

# response = requests.put(url=put_pixel_endpoint, json=put_params, headers=headers)

# response = requests.delete(url=put_pixel_endpoint, headers=headers)
# print(response.text)
