class Query:

    @staticmethod
    def admin_login() -> str:
        return f"SELECT * FROM admin WHERE username = %s and password = %s"

    @staticmethod
    def add_book() -> str:
        return f"INSERT INTO books VALUES (%s, %s, %s, %s)"

    @staticmethod
    def view_all_books() -> str:
        return f"SELECT * FROM books"

    @staticmethod
    def update_book() -> str:
        return f'UPDATE books set book_name = %s, isbn = %s, author = %s, edition = %s WHERE ' \
               f'book_name = %s'

    @staticmethod
    def delete_book() -> str:
        return "DELETE FROM books WHERE book_name = %s"

    @staticmethod
    def user_login() -> str:
        return "SELECT * FROM users WHERE username = %s AND password = %s"

    @staticmethod
    def add_user() -> str:
        return "INSERT INTO users VALUES (%s, %s, %s, %s)"
