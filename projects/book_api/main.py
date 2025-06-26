from http.client import HTTPException

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