import pandas as pd
import matplotlib.pyplot as plt
from fontTools.subset import subset

try:
    df = pd.read_json('read_book.json',encoding='utf-8-sig')
    print('===Данные успешно загружены===')
except Exception as error:
    print(f'Ошибка загрузки файла:{error}')
    exit(1)

# Первые 5 строк
print('\n=== Первые пять строк===')
print(df.head())

#Базовая статистика
print('\n Базовая статистика')
print(df['Оценка'].describe())

#Средняя оценка
avg_rating = df['Оценка'].mean()
print(f'\n Средний рейтинг:{avg_rating:.2f}')

# Фильтрация книг с рейтингом >=8
top_books = df[df['Оценка'] >= 8.0]
print(f'\nКниг с рейтингом >=8: {len(top_books)} шт')

top_books.to_csv('top_books.csv', index=False,encoding='utf-8-sig')
df['Оценка'].hist(bins=10,edgecolor='black')
plt.title('Распределение рейтингов книг')
plt.xlabel('Рейтинг')
plt.ylabel('Количество книг')
plt.savefig('ratings_hist.png')
plt.show()
