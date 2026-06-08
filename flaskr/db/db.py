import json
import os

#Maybe use pickle module?

books_path = 'flaskr/db/books.json'
users_path = 'flaskr/db/users.json'

def is_file_empty(file_path):
    return os.path.getsize(file_path) == 0

def load_file(json_file):

    if not is_file_empty(json_file):
        with open(json_file, "r") as file:
            return json.load(file)

def load_users():
    return load_file(users_path)

def load_books():
    return load_file(books_path)


    
