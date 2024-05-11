import requests
from datetime import datetime
import os

API_KEY = os.environ["API_KEY"]
APP_ID = os.environ["APP_ID"]
USERNAME = os.environ["USERNAME"]
PASSWORD = os.environ["PASSWORD"]
SHEET_ENDPOINT = os.environ["SHEET_ENDPOINT"]

api_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

user_data = {
    "query": input("Tell me which exercises you did: "),
    "weight_kg": "90",
    "height_cm": "178",
    "age": "24",
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

today = datetime.now()
print(today.strftime("%Y/%m/%d"))
print(today.strftime("%H:%M:%S"))

response = requests.post(url=api_endpoint, json=user_data, headers=headers)
result = response.json()
# print(result)


responses = []  # Create an empty list to store responses

for exercise in result['exercises']:
    name = exercise['name']
    duration_min = exercise['duration_min']
    nf_calories = exercise['nf_calories']
    # print(f"Exercise: {name}, Duration: {duration_min} minutes, Calories: {nf_calories}")

    # Ran 5k and walked for 20 minutes

    body = {
        "workout": {
            "date": today.strftime("%Y/%m/%d"),
            "time": today.strftime("%H:%M:%S"),
            "exercise": name.title(),
            "duration": duration_min,
            "calories": nf_calories,
        }
    }

    response = requests.post(url=SHEET_ENDPOINT, json=body, auth=(USERNAME, PASSWORD))
    json_data = response.json()
    responses.append(json_data['workout'])

# Print all the workout data
for workout in responses:
    print(workout)

#step 6 - https://gist.github.com/angelabauer/2e147663f998bbcf7b403c6c83f56a14
#Authentication - https://dashboard.sheety.co/projects/663eb7615888777a6b69d8af/auth

# headers = {
#     "Authorization": "Basic c3RlcGhhbmU0ODpKYXRyYXZhczQ4Kg==",
#     "username": USERNAME,
#     "password": PASSWORD,
# }
#
# delete_endpoint = f"{sheety_endpoint}/4"
# response2 = requests.delete(url=delete_endpoint, headers=headers)
# print(response2)
