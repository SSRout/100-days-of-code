import requests
from datetime import datetime

MY_LAT=22.3511148
MY_LONG=78.6677428

coordinate={
    "lat":MY_LAT,
    "lng":MY_LONG,
    "formatted":0
}
response=requests.get(url="http://api.sunrise-sunset.org/json",params=coordinate)
response.raise_for_status()
data=response.json()
print(data)
sunrise=data["results"]["sunrise"]
sunset=data["results"]["sunset"]

print(sunrise.split("T")[1].split(":")[0])
print(sunset.split("T")[1].split(":")[0])
time_now=datetime.now()
print(time_now.hour)


