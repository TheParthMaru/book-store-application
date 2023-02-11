from utils.database import DatabaseConnection
from utils.queries import Query
from models.user import User


class UserController:

    user: User

    def __init__(self):
        self.connection = DatabaseConnection.connect()

    def login(self, username, password):
        cursor = self.connection.cursor()

        try:
            cursor.execute(Query.user_login(), (username, password))
            result = cursor.fetchone()
            if result is not None:
                UserController.user = User(result[0], result[1], result[2], result[3])
                return True
            else:
                return False
        except Exception as error:
            print("File: user_controller -> login()")
            print(f"Message: {error}")
        finally:
            DatabaseConnection.close(self.connection)

    def add_user(self, first_name, last_name, username, password):
        cursor = self.connection.cursor()
        UserController.user.get_password()
        try:
            cursor.execute(Query.add_user(), (first_name, last_name, username, password))
            return True
        except Exception as error:
            print("File: user_controller -> add_user()")
            print(f"Message: {error}")
            return False
        finally:
            self.connection.commit()
            DatabaseConnection.close(self.connection)
