from controllers.admin_controller import AdminController
from views.book_view import BookView


class AdminView:

    @staticmethod
    def admin_login():
        print("Admin Login")
        while True:
            username = input("Enter username: ")
            password = input("Enter password: ")

            admin_controller = AdminController()
            result = admin_controller.login(username, password)

            if result:
                print("Admin login successful")
                AdminView.admin_dashboard()
                break
            else:
                print("Invalid Credentials")
                return

    @staticmethod
    def admin_dashboard():
        print("\nWelcome Admin")
        while True:
            print("1. Add a new book\n2. View all books\n3. Update a book\n4. Delete a book\n5. "
                  "Logout")

            try:
                choice = int(input("Enter your choice: "))

                if choice == 1:
                    BookView.add_new_book()
                elif choice == 2:
                    BookView.display_all_books()
                elif choice == 3:
                    BookView.update_book()
                elif choice == 4:
                    BookView.delete_book()
                elif choice == 5:
                    print("Logged out")
                    return
                else:
                    print("Invalid choice. Please enter a valid choice")
            except TypeError as error:
                print("Please enter integer values")
                print(error)
