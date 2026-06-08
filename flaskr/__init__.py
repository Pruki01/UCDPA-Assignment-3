from flask import Flask

app = Flask(__name__)

from . import routes
from .db import book, db, user


book1 = book.Book('Book1', 'Author1', 'Genre1', 'Qty1')
book2 = book.Book('Book2', 'Author2', 'Genre2', 'Qty2')

print(db.load_users())
print(db.load_books())
books = db.load_file('flaskr/db/books.json')['books']
print(books)
