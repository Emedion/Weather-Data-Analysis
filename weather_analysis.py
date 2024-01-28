import requests
import pandas as pd

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units' : 'metric'
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()

        temperature = data['main']['temp']
        description = data['weather'][0]['description']
        return city, temperature, description
    except requests.exceptions.RequestException as e:
        return f"Error connecting to OpenWeatherMap API: {e}"
    
api_key = "0f742097a737c47ecf2da205e62a0853"
cities = ['Cairo', 'Lagos', 'Nairobi', 'Accra', 'Johannesburg', 'Casablanca', 
               'Luanda', 'Tunis', 'Cape Town', 'FreeTown', 'Dakar', 'Lome'
               'Kano', 'Maputo', 'Conakry', 'Gaborone', 'Bamako', 'Lusaka', 'Maseru', 'Kigali', 'Kumasi', 'Banjul', 'Bangui'
               ]
column_names = ['Cities ', 'Temp (°C)', 'Description']
weather_data = []
for city in cities:
    data = get_weather(api_key, city)
    if 'Error connecting to OpenWeatherMap API' in data:
        continue
    weather_data.append(data)

df = pd.DataFrame(weather_data, columns=column_names)
print(df)
df.to_csv('weather_data.csv')

