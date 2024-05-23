import requests
from twilio.rest import Client

api_key = "notmyapikey"
OWM_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
account_sid = "notmyaccountsid"
auth_token = "notmyauthtoken"


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
        from_="+notmphonenumber",
        to="++notmphonenumber"
    )
    print(message.status)

