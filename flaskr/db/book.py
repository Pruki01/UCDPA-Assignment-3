from uuid import uuid4
class Book:

    def __init__(self, title, author, img, genre, qty):
        self._isbn      = uuid4()
        self._title     = title 
        self._author    = author
        self._img       = img
        self._genre     = genre
        self._qty       = qty

    def get_isbn(self):
        return self._isbn

    def get_title(self):
        return self._title

    def get_author(self):
        return self._author

    def get_img(self):
        return self._img

    def get_genre(self):
        return self._genre

    def get_qty(self):
        return self._qty
        
    def print_details(self):
        print(f"ISBN: {self._isbn}")
        print(f"Title: {self._title}")
        print(f"Author: {self._author}")
        print(f"Image: {self._img}")
        print(f"Genre: {self._genre}")
        print(f"Quantity: {self._qty}")

    def to_json(self):
        return {
                "Title": self._title,
                "Author": self._author,
                "Image": self._img,
                "Genre": self._genre,
                "Qty": self._qty
            }