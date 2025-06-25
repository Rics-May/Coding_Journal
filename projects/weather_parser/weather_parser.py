import json
import requests
import config
import datetime
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler('weather.log',encoding='utf-8'),logging.StreamHandler()])
logger = logging.getLogger(__name__)

def get_weather_coord(lat, lon, key):
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&lang=ru&appid={key}'
    try:
        response = requests.get(url)
        response.raise_for_status()
        logger.debug('Успешно')
        return response.json()
    except requests.exceptions.RequestException as error:
        logger.error(f'Ошибка при запросе API:{error}', exc_info=True)
        print(f'ошибка при запросе API: {error}')
        return None


def filter_weather_data(data):
    try:
        if not data:
            logger.warning('Получены пустые данные о погоде')
            return None

        rezult = {
            'city': data.get('name', 'Неизвестно'),
            'temp': data.get('main',{}).get('temp','Нет данных'),
            'conditions': [weather['description'] for weather in data.get('weather',[])],
            'timestamp': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        logger.info('Данные отфильтрованы')
        return rezult
    except Exception as e:
        logger.error(f'Ошибка при фильтрации данных:{e}', exc_info=True)
        return None


def create_json(data, json_file):
    try:
        with open(json_file, 'w', encoding='utf-8-sig') as file:
            json.dump(data, file, indent=3,ensure_ascii=False)
        logger.info('Данные сохранены в JSON')
    except Exception as e:
        logger.error(f'Ошибка при сохранении в JSON:{e}', exc_info=True)


def main():
    logger.info('===Запуск программы===')

try:
    logger.debug('Попытка подключения к API погоды')
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={config.lat}&lon={config.lon}&units=metric&lang=ru&appid={config.key}', timeout=10) # Ждать не более 10 секунд
    response.raise_for_status()
except requests.exceptions.Timeout as e:
    logger.critical(f'Ошибка подключения {e}')

data = get_weather_coord(config.lat, config.lon, config.key)
filter_data = filter_weather_data(data)

if filter_data:
        print("Текущая погода:")
        print(f"Город: {filter_data['city']}")
        print(f"Условия: {(filter_data['conditions'])}")
        print(f"Время запроса: {filter_data['timestamp']}")
        if filter_data['temp'] >= 0:
            print(f"Температура: {filter_data['temp']}°C")
        else:
            print(f'Температура минус {abs(filter_data['temp'])}')
else:
    print("Не удалось обработать данные о погоде")

create_json(filter_data,'weather_my_sity.json')
