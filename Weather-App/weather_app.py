
import tkinter as tk

import requests
API_KEY = "enter yours API"



def get_weather():
    city = city_entry.get()

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    data = requests.get(url).json()

    if data["cod"] == 200:
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        condition = data["weather"][0]["description"]
        wind = data["wind"]["speed"]

        temp_label.config(text=f"{temp}°C")
        city_label.config(text=city)
        condition_label.config(text=condition.title())
        humidity_label.config(text=f"Humidity: {humidity}%")
        wind_label.config(text=f"Wind: {wind} m/s")
    else:
        city_label.config(text="City not found!")


root = tk.Tk()
root.title("Weather App")
root.geometry("400x500")
root.configure(bg="#1E293B")

# Title
title = tk.Label(
    root,
    text="🌤 Weather App",
    font=("Arial", 22, "bold"),
    bg="#1E293B",
    fg="white"
)
title.pack(pady=20)

# Search Frame
search_frame = tk.Frame(root, bg="#1E293B")
search_frame.pack(pady=10)

city_entry = tk.Entry(
    search_frame,
    font=("Arial", 14),
    width=20
)
city_entry.grid(row=0, column=0, padx=5)

search_btn = tk.Button(
    search_frame,
    text="Get Weather",
    font=("Arial", 12),
    bg="#3B82F6",
    fg="white",
    command=get_weather
)
search_btn.grid(row=0, column=1)

# Weather Card
card = tk.Frame(
    root,
    bg="#334155",
    width=320,
    height=280
)
card.pack(pady=30)
card.pack_propagate(False)

icon_label = tk.Label(
    card,
    text="☁️",
    font=("Arial", 50),
    bg="#334155",
    fg="white"
)
icon_label.pack(pady=10)

temp_label = tk.Label(
    card,
    text="--°C",
    font=("Arial", 30, "bold"),
    bg="#334155",
    fg="white"
)
temp_label.pack()

city_label = tk.Label(
    card,
    text="City Name",
    font=("Arial", 18),
    bg="#334155",
    fg="white"
)
city_label.pack()

condition_label = tk.Label(
    card,
    text="Weather Condition",
    font=("Arial", 14),
    bg="#334155",
    fg="white"
)
condition_label.pack(pady=10)

humidity_label = tk.Label(
    card,
    text="Humidity: --%",
    font=("Arial", 12),
    bg="#334155",
    fg="white"
)
humidity_label.pack()

wind_label = tk.Label(
    card,
    text="Wind: -- km/h",
    font=("Arial", 12),
    bg="#334155",
    fg="white"
)
wind_label.pack()

root.mainloop()
