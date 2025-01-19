import requests
from configparser import ConfigParser
from tkinter import *
from tkinter import messagebox

config_file = "config.ini"
config = ConfigParser()
config.read(config_file)
api_key = config['gfg']['api']
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'


def getweather(city):
    result = requests.get(url.format(city, api_key))

    if result:
        json = result.json()
        city = json['name']
        country = json['sys']['country']
        temp_kelvin = json['main']['temp']
        temp_celsius = temp_kelvin - 273.15
        weather1 = json['weather'][0]['main']
        return [city, country, temp_kelvin, temp_celsius, weather1]


def search():
    city = city_text.get()
    weather = getweather(city)
    if weather:
        location_lbl['text'] = f'{weather[0]}, {weather[1]}'
        temperature_label['text'] = f"{weather[3]:.2f} °C"
        weather_l['text'] = weather[4]
    else:
        messagebox.showerror('Error', f"Cannot find {city}")


app = Tk()
app.title("Weather App")
app.geometry("400x400")
app.resizable(False, False)

city_text = StringVar()
city_entry = Entry(app, textvariable=city_text, font=("Arial", 14), width=25)
city_entry.pack(pady=20)

Search_btn = Button(app, text="Search Weather", width=20, height=2, font=("Arial", 12), command=search)
Search_btn.pack(pady=10)

location_lbl = Label(app, text="Location", font=('Arial', 20, 'bold'))
location_lbl.pack(pady=10)

temperature_label = Label(app, text="", font=('Arial', 16))
temperature_label.pack(pady=5)

weather_l = Label(app, text="", font=('Arial', 14))
weather_l.pack(pady=5)

app.mainloop()
