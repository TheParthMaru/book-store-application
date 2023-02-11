class Book:
    def __init__(self, book_name, isbn, author, edition):
        self.__book_name = book_name
        self.__isbn = isbn
        self.__author = author
        self.__edition = edition

    def __int__(self, book_name):
        self.__book_name = book_name

    def get_book_name(self):
        return self.__book_name

    def set_book_name(self, book_name):
        self.__book_name = book_name

    def get_isbn(self):
        return self.__isbn

    def set_isbn(self, isbn):
        self.__isbn = isbn

    def get_author(self):
        return self.__author

    def set_author(self, author):
        self.__author = author

    def get_edition(self):
        return self.__edition

    def set_edition(self, edition):
        self.__edition = edition
