from controllers.user_controller import UserController


class UserView:
    @staticmethod
    def user_login():
        print("\nUser Login")
        while True:
            username = input("Enter your username: ")
            password = input("Enter your password: ")

            user_controller = UserController()
            result = user_controller.login(username, password)

            if result:
                print("Logged in")
                break
            else:
                print("Invalid credentials or user does not exists")
                print("1. Create a new user\n2. Retry login")
                choice = int(input("Enter your choice: "))

                if choice == 1:
                    print("Will be redirecting to create user view")
                    UserView.create_user()
                    break
                elif choice == 2:
                    continue
                else:
                    print("Invalid choice. Please enter a valid choice")

    @staticmethod
    def create_user():
        while True:
            print("\nCreate a new user")
            first_name = input("Enter your first name: ")
            last_name = input("Enter your last name: ")
            user_name = input("Create your user name: ")
            password = input("Create your password: ")

            user_controller = UserController()

            result = user_controller.add_user(first_name, last_name, user_name, password)

            if result:
                print("User created successfully")
                break
            else:
                print("Failed to create new user")
