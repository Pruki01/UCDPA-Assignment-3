from flask import render_template 
from flaskr import app
from flaskr.db import db, book

book1 = book.Book('Title', 'Author', '/static/images/spongebob.jpg', 'Genre', 'QTY').to_json()
book2 = book.Book('Title1', 'Author1', '/static/images/spongebob.jpg', 'Genre1', 'QTY1').to_json()
book3 = book.Book('Title2', 'Author2', '/static/images/spongebob.jpg', 'Genre2', 'QTY2').to_json()

books_json = db.load_books()
books = books_json['books']
books.append(book1)
books.append(book2)
books.append(book3)
print(books)

@app.route('/')
def index():
    return render_template('index.html', book_list=books)

@app.route('/<uuid:ISBN>')
def book_page(ISBN):
    book = db.load_book(ISBN, books)
    
    print(f"This book is being used {book}")
    if book is None:
        abort(404)
    else:
        return render_template('book.html', book=book)