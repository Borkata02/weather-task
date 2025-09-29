import requests
import random

API_KEY = "c44727b431e8a12e8b019b9fdf9bb4a4"

cities = ["Sofia", "London", "New York", "Tokyo", "Paris"]
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


