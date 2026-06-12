from flaskr import app
from flaskr.db import db, user, book
from flask import(
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

@app.route('/')
def index():
    print(db.load_books())
    return render_template('index.html', book_list=db.load_books())

@app.route('/<uuid:ISBN>')
def book_page(ISBN):
    books = db.load_books()
    book = db.load_book(ISBN, books)

    if book is None:
        flash('The book you are looking for doesn\'t exist!')
    else:
        return render_template('book.html', book=book)

@app.route('/register')
def register():
    return render_template('auth/register.html')

@app.route('/login')
def login():
    return render_template('auth/login.html')

if __name__ == "__main__":
    app.run(debug=True, port=5000)