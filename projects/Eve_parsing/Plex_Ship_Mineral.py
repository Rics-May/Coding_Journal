import time
import requests
import pandas as pd

from projects.Eve_parsing.Config import BASE_URL, REGION_ID, MINERALS, BATTLESHIP, MARADERS , PLEX


def market_data(region_id, type_id):
    url = BASE_URL.format(REGION_ID, item_id)
    try:
        response = requests.get(url)
        data = response.json()
        df = pd.DataFrame(data)
        df['item_id'] = item_id
        time.sleep(1)
        return df
    except Exception as error:
        print(f'Ошибка подключения к API:{error}')

all_data = []
for item_id in MINERALS + BATTLESHIP + MARADERS + PLEX:
    print(f'=== Загрузка данных для {item_id} ===')
    df = market_data(REGION_ID,item_id)
    if not df.empty:
        all_data.append(df)

if all_data:
    final_df = pd.concat(all_data, ignore_index=True)
    item_names = {
        34: "Tritanium", 35: "Pyerite", 36: "Mexallon", 37: "Isogen",
        38: "Nocxium", 39: "Zydrine", 40: "Megacyte", 11399: "Morphite",
        24692: "Abbadon", 24694: "Maelstorm",
        24696: "Apocalypse", 645: "Dominix",
        28659: "Paladin", 28665: "Vargur", 28661: "Kronos", 28710: "Golem",
        44992: "Plex", 644: "Typhoon",
        639: "Tempest", 642: "Apocalypse", 643: "Armageddon",
        640: "Scorpion", 24688: "Rokh", 638: "Raven", 641: "Megathron",
        24690: "Hyperion"
    }
    final_df['item_name'] = final_df['item_id'].map(item_names)
    final_df.to_csv('Eve_Price_to_DS.csv')
    final_df.to_json('Eve_Price_to_DS.json')
    print('=== Данные загружены в файл! ===')
else:
    print('Нет Данных')
