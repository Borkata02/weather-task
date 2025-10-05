import tkinter as tk
from tkinter import messagebox
import requests

API_KEY = "c44727b431e8a12e8b019b9fdf9bb4a4"

#Main logic function
def get_weather():
    city = city_entry.get()
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data.get("cod") != 200:
        messagebox.showerror("Error", f"City '{city}' not found. Please try again.")
    else:
        weather = data["weather"][0]["description"].title()
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]


        result_label.config(text=f"Weather: {weather}\nTemperature: {temp} °C\nHumidity: {humidity}%")

# Main window
root = tk.Tk()
root.title("Weather App")
root.geometry("300x200")

# Input
city_label = tk.Label(root, text="Enter city:")
city_label.pack(pady=5)

city_entry = tk.Entry(root, width=30)
city_entry.pack(pady=5)

# Button
check_button = tk.Button(root, text="Check Weather", command=get_weather)
check_button.pack(pady=5)

# Result
result_label = tk.Label(root, text="", font=("Arial", 10))
result_label.pack(pady=10)

root.mainloop()
