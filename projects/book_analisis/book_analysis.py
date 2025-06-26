import pandas as pd

try:
    df = pd.read_json('read_book.json',encoding='utf-8-sig')
    print('===Данные успешно загружены===')
except Exception as error:
    print(f'Ошибка загрузки файла:{error}')
    exit(1)

print('\n=== Первые пять строк===')
print(df.head())

print('\n Базовая статистика')
print()