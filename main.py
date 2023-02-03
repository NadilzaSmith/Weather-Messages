import requests
from twilio.rest import Client
import os



MY_LATITUDE = 33.748997
MY_LONGITUDE = -84.387985
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
MY_NUMBER = "+12562557703"

account_sid = "ACc0cbc801fafef3f9ab2b77635b20d350"
auth_token = os.environ.get("TOKEN_KEY")

api_key = os.environ.get("OWM_KEY")

parameters = {
    "lat": MY_LATITUDE,
    "log": MY_LONGITUDE,
    "exclude": "alerts",
    "appid": api_key
}

rain = False

response = requests.get(OWM_ENDPOINT, params=parameters)
response.raise_for_status()
data = response.json()
slice_data = data["hourly"][:12]

for hour_data in slice_data:
    weather_condition = hour_data["weather"][0]["id"]
    if int(weather_condition) < 700:
        rain = True
if rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="Its, going rain today,you need an umbrella",
        from_="+12562557703",
        to="+17707907932"
    )

