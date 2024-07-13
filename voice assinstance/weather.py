import requests, json

apiKey = "3825af9e74068a9af623c519e82fe299"

baseURL = "https://api.openweathermap.org/data/2.5/weather?q="

city = input("Enter your city name: ")

CompleteURL = baseURL + city + "&appid=" + apiKey

response = requests.get(CompleteURL)

data = response.json()

print("Current Temperature:",data["main"]["temp"])
print("Current Temperature feels like:",data["main"]["feels_like"])
print("Maximun Temperature:",data["main"]["temp_max"])
print("Minimun Temperature:",data["main"]["temp_min"])