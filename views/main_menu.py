from views.admin_view import AdminView
from views.user_view import UserView


class MainMenu:
    @staticmethod
    def display_menu():
        while True:
            print("***Welcome To Parth's Book Store***")
            print("1. Login as admin\n2. Login as user\n3. Create a user\n4. Exit")

            try:
                choice = int(input("Enter your choice: "))

                if choice == 1:
                    # Go to admin view
                    AdminView.admin_login()
                elif choice == 2:
                    # Go to user login in user view
                    UserView.user_login()
                elif choice == 3:
                    UserView.create_user()
                elif choice == 4:
                    print("Thank you!!!")
                    return
                else:
                    print("Invalid choice. Please enter a valid choice")
            except TypeError:
                print("Please enter integer values")
