import requests
from twilio.rest import Client

api_key = "d9ff5f43fd612f1092a864ab4af377a7"
OWM_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
account_sid = "AC92f77f85973027db2c34dc69ee94b8b4"
auth_token = "6e9d4e4bcb07461f76d0585cd846f6b0"


weather_params = {
    "lat": 41.135891,
    "lon": -8.633180,
    "appid": api_key
}

weather_params2 = {
    "q": "Vila Nova de Gaia,portugal",
    "cnt": 4,
    "appid": api_key
}

# https://api.openweathermap.org/data/2.5/weather?lat={41.135891}&lon={-8.633180}&appid={api_key}
# http://api.openweathermap.org/data/2.5/weather?q=Vila Nova de Gaia,portugal&APPID=api_key

response = requests.get(OWM_endpoint, params=weather_params2)
response.raise_for_status()
data = response.json()

will_rain = False
for hour_data in data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Leva chuço, rei ☂️",
        from_="+17084809890",
        to="+351968959727"
    )
    print(message.status)

