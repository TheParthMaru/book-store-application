from tabulate import tabulate
from controllers.book_controller import BookController


class BookView:

    @staticmethod
    def add_new_book():
        book_name = input("Enter book name: ")
        isbn = int(input("Enter isbn: "))
        author = input("Enter author: ")
        edition = int(input("Enter edition: "))

        book_controller = BookController()
        result = book_controller.add_book(book_name, isbn, author, edition)

        if result:
            print("Book added successfully")
        else:
            print("Failed to add book")

    @staticmethod
    def display_all_books():
        book_controller = BookController()
        result = book_controller.view_all_books()
        print()
        print(tabulate(result, headers=["Book Name", "ISBN", "Author", "Edition"]))
        print()

    @staticmethod
    def update_book():
        print("\nUpdate Book")
        book_name = input("Enter book name: ")
        isbn = int(input("Enter isbn: "))
        author = input("Enter author: ")
        edition = int(input("Enter edition: "))

        book_controller = BookController()
        result = book_controller.update_book(book_name, isbn, author, edition)

        if result:
            print("Book updated successfully")
        else:
            print("Failed to update book")

    @staticmethod
    def delete_book():
        print("\nDelete book")
        book_name = input("Enter book name: ")
        book_controller = BookController()
        result = book_controller.delete_book(book_name)

        if result:
            print("Book deleted successfully")
        else:
            print("Failed to delete book")
