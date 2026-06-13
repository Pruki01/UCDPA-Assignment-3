import json
import os
from werkzeug.security import generate_password_hash

books_path = 'flaskr/db/books.json'
users_path = 'flaskr/db/users.json'

# Loading file
def is_file_empty(file_path):
    return os.path.getsize(file_path) == 0

def load_file(json_file):

    try:
        if os.path.exists(json_file) and not is_file_empty(json_file):
            with open(json_file, "r") as file:
                return json.load(file)
        else:
            return None
    except OSError:
        print("File Missing!")

# Saving file
def write_db(json_file, json_data):

    if os.path.exists(json_file):
        with open(json_file, "w") as file:
            json.dump(json_data, file, indent=4)

# Users
def user_exists(user):

    current_users = load_users()
    if str(user.get_id()) in current_users:
        return True
    else:
        return False

def load_users():
    return load_file(users_path)

def load_user(email):

    current_users = load_users()
    print(current_users)
    if email in current_users:
        return current_users[email]
    else:
        return None

def write_users(json_data):
    write_db(users_path, json_data)

def add_user(user):
    
    if not user_exists(user):
        current_users = load_users()
        current_users[user.get_email()] = user.to_json()
        write_users(current_users)

def change_password(user_id, new_password):
    current_users = load_users()
    if user_id in current_users:
        current_users[id]['Password'] = generate_password_hash(new_password)

def remove_user(user):

    current_users = load_users()
    if str(user.get_id()) in current_users:
        del current_users[str(user.get_id())]

# Book
def load_books():
    return load_file(books_path)

def load_book(ISBN):
    current_books = load_books()
    ISBN = str(ISBN)

    if ISBN in current_books:
        return current_books[ISBN]
    else:
        return None
    
def write_books(json_data):
    write_db(books_path, json_data)

def add_book(book):

    books = load_books()
    if not book.get_isbn() in books:
        books[str(book.get_isbn())] = book.to_json()
        write_books(books)

def update_book(isbn):
    pass

def remove_book(isbn):
    current_books = load_books()
    if isbn in current_books:
        del current_books[isbn]

    
