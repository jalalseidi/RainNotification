import requests
from twilio.rest import Client

twilio_apikey = "<>"
API_KEY = "<>"
MY_LAT = 41.089790
MY_LONG = -91.255569
auth_token = "<>"
account_sid = "<>"
parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "cnt": 4,
    "units": "metric",
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
data = response.json()

will_rain = False
for forecast in data["list"]:
    weather = forecast["weather"][0]["id"]
    if int(weather) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring a broly.",
        from_="<>",
        to="<>",
    )
    print(message.status)
