import requests
import datetime as dt


MY_LAT = 39.654251
MY_LNG = -106.823601

# response = requests.get('http://api.open-notify.org/iss-now.json')
# # The raise_for_status() method will raise an HTTPError if the HTTP request returned an unsuccessful status code.
# response.raise_for_status()
#
# data = response.json()
#
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
#
# iss_position = (longitude, latitude)
# print(iss_position)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0.
}
lat = parameters["lat"]
lng = parameters["lng"]

# https://api.sunrise-sunset.org/json?lat=39.654251&lng=-106.823601

response = requests.get("https://api.sunrise-sunset.org/json?", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)

current_time = dt.datetime.now()

print(current_time.hour)

# {'results': {'sunrise': '11:54:04 AM', 'sunset': '2:13:14 AM', 'solar_noon': '7:03:39 PM', 'day_length': '14:19:10', 'civil_twilight_begin': '11:25:24 AM', 'civil_twilight_end': '2:41:54 AM', 'nautical_twilight_begin': '10:48:14 AM', 'nautical_twilight_end': '3:19:04 AM', 'astronomical_twilight_begin': '10:07:26 AM', 'astronomical_twilight_end': '3:59:52 AM'}, 'status': 'OK'}
