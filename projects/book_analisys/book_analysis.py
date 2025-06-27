import pandas as pd
import matplotlib.pyplot as plt
from fontTools.ttLib.woff2 import bboxFormat


# Функции загрузки JSON для скрипта
def load_file(file_path):
    try:
        df = pd.read_json('read_book.json',encoding='utf-8-sig')
        print('===Данные успешно загружены===')

        if 'Оценка' not in df.columns:
            raise KeyError('Столбец "Оценка" не найден')
        df['Оценка'] = pd.to_numeric(df['Оценка'], errors='coerce')
        df.dropna(subset=['Оценка']) # Удаление строк с некорректными данными
        return df
    except Exception as error:
        print(f'Ошибка загрузки файла:{error}')
        exit(1)
def book_analisys(df):
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

# Сохранение в CSV
    top_books.to_csv('top_books.csv', index=False,encoding='utf-8-sig')
# Гистограмма

    df['Оценка'].hist(bins=10,edgecolor='black',grid=False)
    plt.title('Распределение рейтингов книг', pad=20)
    plt.xlabel('Рейтинг', labelpad=10)
    plt.ylabel('Количество книг', labelpad=10)
    plt.savefig('ratings_hist.png')
    plt.show()

    top_authors = df['Автор'].value_counts().head(5)
    top_authors.plot.pie(autopct='%1.1f%%')
    plt.title('Топ 5 авторов')
    plt.savefig('top_authors.png')
if __name__== "__main__":
    df = load_file('read_book.json')
    book_analisys(df)
