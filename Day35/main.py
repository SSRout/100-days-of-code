import requests
from twilio.rest import Client

Owm_endPoint="https://api.openweathermap.org/data/2.5/onecall"
api_key="12vhjg32bv4hg3v53bv5h345"#your key
#twillio id
account_sid="JKHSDKJFBUJWHEBFJBJMBFJ242JHGJKH"
auth_token="4356hjkgjhgj634g6jh34bjhgj"

weather_params={
    "lat":0000,#your values
    "lon":0000,
    "appid":api_key,
    "excllude":"current,minutely,daily"
}
response=requests.get(Owm_endPoint,params=weather_params)
print(response.status_code)
response.raise_for_status()
weather_data=response.json()

weather_slice=weather_data["hourly"][:12]

will_rain=False
for hour_data in weather_slice:
    condition_code=hour_data["weather"][0]["id"]
    if int(condition_code)<700:
       will_rain=True

if will_rain:
    #print("Bring umbrella.")
    client=Client(account_sid,auth_token)
    message=client.messages.create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_="YOUR TWILIO VIRTUAL NUMBER",
        to="YOUR TWILIO VERIFIED REAL NUMBER"
    )
print(message.status)