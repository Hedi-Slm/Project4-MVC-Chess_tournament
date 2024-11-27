class MainView:
    @staticmethod
    def show_main_menu():
        print("What would you like to do?")
        print("1. Player Menu")
        print("2. Tournament Menu")
        print("3. Report Menu")
        print("4. Exit")

    @staticmethod
    def get_user_choice():
        return input("Enter your choice: ")
