import requests
import random

API_KEY = "c44727b431e8a12e8b019b9fdf9bb4a4"

cities = [
    "Sofia", "London", "New York", "Tokyo", "Paris",
    "Berlin", "Madrid", "Rome", "Moscow", "Beijing",
    "Sydney", "Cairo", "Dubai", "Toronto", "Los Angeles",
    "Rio de Janeiro", "Buenos Aires", "Mexico City", "Johannesburg", "Istanbul",
    "Athens", "Warsaw", "Prague", "Vienna", "Budapest",
    "Seoul", "Bangkok", "Singapore", "Kuala Lumpur", "Jakarta",
    "Helsinki", "Oslo", "Stockholm", "Copenhagen", "Reykjavik",
    "Lisbon", "Dublin", "Brussels", "Zurich", "Edinburgh"
]

selected_cities = random.sample(cities, 5)
temps = {}

print("Weather for 5 random cities:\n")

for city in selected_cities:
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    weather = data["weather"][0]["description"]
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]

    temps[city] = temp

    print(f"\033[1m{city}\033[0m: {weather} \n Temp: {temp} °C \n Humidity: {humidity}%")

coldest_city = min(temps, key=temps.get)
average_temp = sum(temps.values()) / len(temps)

print("\nStatistics:")
print(f"Coldest city: {coldest_city} ({temps[coldest_city]} °C)")
print(f"Average temperature: {average_temp:.2f} °C")

#User Input
while True:
    user_city = input("\nEnter a city to check the weather: ")

    url = f"http://api.openweathermap.org/data/2.5/weather?q={user_city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data.get("cod") != 200:
        print(f"City '{user_city}' not found. Please try again.")
    else:
        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]

        print(f"\033[1m{user_city}\033[0m: {weather} \n Temp: {temp} °C \n Humidity: {humidity}%")
        break
