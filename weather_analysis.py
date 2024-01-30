import requests
import pandas as pd
import random


def  populate_city():
    file_path = "cities_list.xlsx"
    dataFrame = pd.read_csv("C:/Users/USER/OneDrive/Documents/Workspace/code/2024/cities_list1.csv")

    num_rows = dataFrame.shape[0]
    column_names = ['country', 'name']
    random_cells = {}
    for columns in range(200):
        row = random.randint(0, num_rows-1) # select a random row number between 0 and the last row of the DataFrame
        key = dataFrame.at[row, column_names[0]]
        value = dataFrame.at[row, column_names[1]]
        random_cells[key] = value
    return random_cells


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
        country  = data["sys"]["country"]
        return country, city, temperature, description
    except requests.exceptions.RequestException as e:
        return f"Error connecting to OpenWeatherMap API: {e}"
    
api_key = "0f742097a737c47ecf2da205e62a0853"
# cities = ['Cairo', 'Lagos', 'Nairobi', 'Accra', 'Johannesburg', 'Casablanca', 
#                'Luanda', 'Tunis', 'Cape Town', 'FreeTown', 'Dakar', 'Lome'
#                'Kano', 'Maputo', 'Conakry', 'Gaborone', 'Bamako', 'Lusaka', 'Maseru', 'Kigali', 'Kumasi', 'Banjul', 'Bangui'
#                ]

cities = {}


if not cities:
    cities = populate_city()
    print(cities)
column_names = ['Country', 'Cities ', 'Temp (°C)', 'Description']
weather_data = []
for city in cities:
    data = get_weather(api_key, cities[city])
    if 'Error connecting to OpenWeatherMap API' in data:
        continue
    weather_data.append(data)

df = pd.DataFrame(weather_data, columns=column_names)
print(df)
df.to_csv('weather_data.csv')

