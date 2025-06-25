import json
import requests
import config
import datetime
def get_weather_coord(lat, lon, key):
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&lang=ru&appid={key}'
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as error:
        print(f'ошибка при запросе API: {error}')
        return None

def filter_weather_data(data):
    rezult = {
        'city': data.get('name', 'Неизвестно'),
        'temp': data.get('main',{}).get('temp','Нет данных'),
        'conditions': [weather['description'] for weather in data.get('weather',[])],
        'timestamp': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    return rezult

def create_json(data, json_file):
    with open(json_file, 'w', encoding='utf-8-sig') as file:
        json.dump(data, file, indent=3,ensure_ascii=False)

data = get_weather_coord(config.lat, config.lon, config.key)
filter_data = filter_weather_data(data)
if filter_data:
        print("Текущая погода:")
        print(f"Город: {filter_data['city']}")
        print(f"Температура: {filter_data['temp']}°C")
        print(f"Условия: {', '.join(filter_data['conditions'])}")
        print(f"Время запроса: {filter_data['timestamp']}")
else:
    print("Не удалось обработать данные о погоде")

create_json(filter_data,'weather_my_sity.json')
