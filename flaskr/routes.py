from flask import render_template
from flaskr import app
from flaskr.db import db, book

book1 = book.Book('Title', 'Author', 'Genre', 'QTY').to_json()
book2 = book.Book('Title1', 'Author1', 'Genre1', 'QTY1').to_json()
book3 = book.Book('Title2', 'Author2', 'Genre2', 'QTY2').to_json()

books_json = db.load_books()
books = books_json['books']

@app.route("/")
def hello_wolrd():
    return render_template('index.html', book_list=books)