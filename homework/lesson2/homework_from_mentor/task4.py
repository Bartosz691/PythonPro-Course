weather_data = [{'temp': 12, 'rain': False},
                {'temp': 15, 'rain': False},
                {'temp': 14, 'rain': True},
                {'temp': 18, 'rain': False},
                {'temp': 20, 'rain': True},
                {'temp': 19, 'rain': False},
                {'temp': 24, 'rain': False},
                {'temp': 21, 'rain': True},
                {'temp': 18, 'rain': True},
                {'temp': 17, 'rain': False},
                {'temp': 24, 'rain': False},
                ]

def is_nice_weather(temp: int, rain: bool) -> bool:
    if 15 <= temp <= 25 and rain == False:
        return True
    else:
        return False

licznik = 0   

for day in weather_data:
    if is_nice_weather(day['temp'], day['rain']):
       licznik +=1

print(f"Ilość ładnych dni wynosi: {licznik}")