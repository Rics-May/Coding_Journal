import  csv
import json
import logging

logging.basicConfig(level=logging.INFO)

def convert_csv_to_json(csv_file, json_file):
    try:
        with (open(csv_file, 'r', newline='',encoding='windows-1251') as file):
            book_data = []
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:
                row['Оценка'] = float(row['Оценка'])
                book_data.append(row)
            logging.info(f'Прочитано {len(book_data)} записей из CSV')

        with open(json_file, 'w', encoding='utf-8-sig') as fi:
            json.dump(book_data, fi, indent=3, ensure_ascii=False)
            logging.info(f'Данные успешно записаны в {json_file}')
    except FileNotFoundError:
        logging.error(f'Файл {csv_file} не найден')
    except Exception as e:
        logging.error(f'Ошибка при конвертации {str(e)}')

convert_csv_to_json('read_book.csv', 'read_book.json')
convert_csv_to_json('Eve_Price_to_DS.csv', 'Eve_Price_to_DS.json')


