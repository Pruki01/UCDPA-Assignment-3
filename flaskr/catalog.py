import functools

from flask import(
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from werkzeug.security import check_password_hash, generate_password_hash
from flaskr.db import db, book

bp = Blueprint('catalog', __name__,)

@bp.route('/')
def index():
    print(db.load_books())
    return render_template('index.html', book_list=db.load_books()['books'])

@bp.route('/<uuid:ISBN>')
def book_page(ISBN):
    books = db.load_books()['books']
    book = db.load_book(ISBN, books)

    if book is None:
        flash('The book you are looking for doesn\'t exist!')
    else:
        return render_template('book.html', book=book)
