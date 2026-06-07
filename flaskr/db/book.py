class Book:

    def __init__(self, isbn, name, author, genre, qty):
        self._isbn      = isbn
        self._name      = name
        self._author    = author
        self._genre     = genre
        self._qty       = qty

    def get_isbn(self):
        return self._isbn

    def get_name(self):
        return self._name

    def get_author(self):
        return self._author

    def get_genre(self):
        return self._genre

    def get_qty(self):
        return self._qty