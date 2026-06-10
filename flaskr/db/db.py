import json
import os

#Maybe use pickle module?

books_path = 'flaskr/db/books.json'
users_path = 'flaskr/db/users.json'

def is_file_empty(file_path):
    return os.path.getsize(file_path) == 0

def load_file(json_file):

    if os.path.exists(json_file) and not is_file_empty(json_file):
        with open(json_file, "r") as file:
            return json.load(file)

def load_users():
    return load_file(users_path)

def load_books():
    return load_file(books_path)

def load_book(ISBN, book_list):
    print(book_list)
    for book in book_list:
        if book['ISBN'] == str(ISBN):
            return book

    return None 

def write_db(json_file, json_data):

    if os.path.exists(json_file):
        with open(json_file, "w") as file:
            json.dump(json_data, file, indent=4)

def write_users(json_data):
    write_db(users_path, json_data)
    
def write_books(json_data):
    write_db(books_path, json_data)
    
