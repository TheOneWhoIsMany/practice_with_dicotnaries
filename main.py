# working with apis and dictionaries
import requests
import json
response = requests.get("https://randomuser.me/api")

# print(response.json())

title = response.json()['results'][0]['name']['first']
print(title)
gender = response.json()['results'][0]['gender']
print(gender)
last_name = response.json()['results'][0]['name']['last']
print(last_name)
street = response.json()['results'][0]['location']['street']['name']
print(street)
city = response.json()['results'][0]['location']['city']
print(city)
state = response.json()['results'][0]['location']['state']
print(state)
postcode = response.json()['results'][0]['location']['postcode']
print(postcode)
email = response.json()['results'][0]['email']
print(email)
username = response.json()['results'][0]['login']['username']
print(username)