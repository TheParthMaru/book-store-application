from utils.database import DatabaseConnection
from utils.queries import Query
from models.book import Book


class BookController:
    def __init__(self):
        self.__connection = DatabaseConnection.connect()

    # Method to add a new book
    def add_book(self, book_name, isbn, author, edition):
        book = Book(book_name, isbn, author, edition)
        try:
            cursor = self.__connection.cursor()
            cursor.execute(Query.add_book(), (book.get_book_name(), book.get_isbn(),
                                              book.get_author(), book.get_edition()))

            return True
        except Exception as error:
            print("BookController -> add_book()")
            print(f"Message: {error}")
            return False
        finally:
            self.__connection.commit()
            DatabaseConnection.close(self.__connection)

    # Method to view all the books
    def view_all_books(self):
        try:
            cursor = self.__connection.cursor()
            cursor.execute(Query.view_all_books())
            result = cursor.fetchall()

            return result
        except Exception as error:
            print("book_controller -> view_all_books()")
            print(f"Message: {error}")
        finally:
            DatabaseConnection.close(self.__connection)

    # Method to update all fields of a book
    def update_book(self, book_name, isbn, author, edition):
        book = Book(book_name, isbn, author, edition)

        try:
            cursor = self.__connection.cursor()
            cursor.execute(Query.update_book(), (book.get_book_name(), book.get_isbn(),
                                                 book.get_author(), book.get_edition(),
                                                 book.get_book_name()))

            return True
        except Exception as error:
            print("BookController -> update_book()")
            print(f"Message: {error}")
            return False
        finally:
            self.__connection.commit()
            DatabaseConnection.close(self.__connection)

    def delete_book(self, book_name):
        book = Book(book_name, 0, "", 0)

        try:
            cursor = self.__connection.cursor()
            cursor.execute(Query.delete_book(), (book.get_book_name(),))

            return True
        except Exception as error:
            print("BookController -> delete_book()")
            print(f"Message: {error}")
            return False
        finally:
            self.__connection.commit()
            DatabaseConnection.close(self.__connection)
