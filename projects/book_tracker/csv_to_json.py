import  csv
import json


def convert_csv_to_json(csv_file, json_file):
    with open(csv_file, 'r', newline='',encoding='windows-1251') as file:
        book_data = []
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            book_data.append(row)

    with open(json_file, 'w', encoding='utf-8-sig') as fi:
        json.dump(book_data, fi, indent=3, ensure_ascii=False)

convert_csv_to_json('read_book.csv', 'read_book.json')



