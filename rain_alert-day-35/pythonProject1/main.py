import requests
from twilio.rest import Client

account_sid = "xxxx"
auth_token = "xxxx"
client = Client(account_sid, auth_token)


OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "xxxx"

weather_params = {
    "lat": 43.653225,
    "lon": 0000,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(url=OWM_Endpoint, params=weather_params)
weather_data = response.json()
# print(weather_data)

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☂️",
        from_='xxxx',
        to='xxxx'
    )
    print(message.status)
