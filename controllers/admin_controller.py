from utils.database import DatabaseConnection
from models.admin import Admin
from utils.queries import Query


class AdminController:
    def __init__(self):
        self.connection = DatabaseConnection.connect()

    # Method for admin login
    def login(self, username, password):
        admin = Admin(username, password)
        try:
            cursor = self.connection.cursor()
            cursor.execute(Query.admin_login(), (admin.get_username(), admin.get_password()))
            result = cursor.fetchone()

            if result is not None:
                return True
            else:
                return False
        except Exception as error:
            print(f"admin_controller -> login()\nMessage: {error}")
        finally:
            DatabaseConnection.close(self.connection)
