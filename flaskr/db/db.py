import json
import os

#Maybe use pickle module?

def is_file_empty(file_path):
    return os.path.getsize(file_path) == 0

def load_file(json_file):

    if not is_file_empty(json_file):
        with open(json_file, "r") as file:
            return json.load(file)
def save_to_file(file, json_data):
    with open(file, "w") as json_file:
        json.dump(json_data, json_file)
    
def save_books(json_file):
    return {
        "users": [json_file]
    }



    
