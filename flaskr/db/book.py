from uuid import uuid5, NAMESPACE_OID
class Book:

    def __init__(self, title, author, img, genre, description, qty):
        self._title         = title 
        self._author        = author
        self._img           = img
        self._genre         = genre
        self._description   = description
        self._qty           = qty
        self._isbn          = uuid5(NAMESPACE_OID, 
                                    f"{self._title}|{self._author}")

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
                "ISBN": str(self._isbn),
                "Title": self._title,
                "Author": self._author,
                "Image": self._img,
                "Genre": self._genre,
                "Description": self._description,
                "Qty": self._qty
            }