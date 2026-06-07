import json

def save_to_file(file, json_data):
    with open(file) as json_file:
        json.dump(json_data, json_file)
