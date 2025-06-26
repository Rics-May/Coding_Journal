from fastapi import HTTPException
from fastapi import Query
from collections import defaultdict
from fastapi import FastAPI
import json
from typing import List, Dict

app = FastAPI(title='Book_API', version='1.0')

with open('read_book.json','r',encoding='utf-8-sig') as file:
    books:List[Dict] = json.load(file)

@app.get('/')
def home() -> Dict:
    return {
        'message': "API для моих прочитанных книг",
        'endpoints': ['/books', '/books/{id}', "/stats"]
    }

@app.get('/books/{book_id}')
def get_book(book_id:int):
    if book_id > len(books) or book_id < 0:
        raise HTTPException(status_code=404, detail = 'Книга не найдена')
    return books[book_id]

@app.get('/books/filter')
def filter_books(
    min_rating: float = Query(..., ge=1, le=10, description="Минимальный рейтинг от 1 до 10"),
    author: str = Query(None)
) -> List[Dict]:
    try:
        filtered_books = [
            book for book in books
            if float(book.get("Оценка","0")) >= min_rating
            and (author is None or book.get("Автор") == author)
        ]
        return filtered_books
    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=f"Некорректный параметр min_rating. Ожидается число, получено: {min_rating}"
        )


@app.get('/stats')
def get_stats() -> Dict:
    # Статистика по авторам
    authors_counts = defaultdict(int)
    for book in books:
        author = book.get("Автор")
        if author:
            authors_counts[author] += 1
    top_author = max(authors_counts.items(), key=lambda x: x[1])[0] if authors_counts else None

    # Статистика по годам
    year_stats = defaultdict(int)
    for book in books:
        date = book.get('Дата')
        if date:
            year = date.split('-')[0]  # Извлекаем год из формата "2025-06"
            year_stats[year] += 1
    top_year = max(year_stats.items(), key=lambda x: x[1])[0] if year_stats else None

    # Средний рейтинг
    average_rating = round(sum(float(book.get('Оценка', '0')) for book in books) / len(books), 2)

    return {
        'total_books': len(books),
        'average_rating': average_rating,
        'top_author': top_author,
        'top_year': top_year
    }
