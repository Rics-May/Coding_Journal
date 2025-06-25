from fastapi import FastAPI
import json

app = FastAPI()

with open('read_book.json','r',encoding='utf-8-sig') as file:
    books = json.load(file)
