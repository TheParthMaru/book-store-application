import psycopg2


class DatabaseConnection:

    @staticmethod
    def connect():
        try:
            connection = psycopg2.connect(
                database="book-store",
                user="parth",
                password="parth",
                host='localhost',
                port=5432
            )

            return connection
        except Exception as error:
            print(f"Location: database.py -> connect()\nMessage: {error}")

    @staticmethod
    def close(connection):
        connection.close()
