from utils.utilities import get_valid_date


class PlayerView:
    @staticmethod
    def show_player_menu():
        print("What would you like to do?")
        print("1. Add player")
        print("2. Show player list")
        print("3. Back to main menu")
        return input("Enter your choice: ")

    @staticmethod
    def show_players_list(players):
        if not players:
            print("No players found.")
            return

        for player in players:
            print(f"{player.first_name} {player.last_name} "
                  f"- ID: {player.chess_id}")

    @staticmethod
    def get_player_id():
        return input("Enter player ID: ")

    @staticmethod
    def get_player_details(chess_id):
        first_name = input("Enter first name of the player: ")
        last_name = input("Enter last name of the player: ")
        birth_date = get_valid_date(
            "Enter birth date of the player (dd/mm/yyyy): "
        )
        return {
            "first_name": first_name,
            "last_name": last_name,
            "birth_date": birth_date.strftime("%d/%m/%Y"),
            "chess_id": chess_id,
        }
